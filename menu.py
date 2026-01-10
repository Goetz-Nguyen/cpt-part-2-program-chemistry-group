import tkinter as tk
from tkinter import ttk, messagebox
import contextlib
import io
import os
from datetime import datetime as dt

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CuriousChemists")
        self.root.geometry("900x560")
        self.root.minsize(820, 520)

        # THEME COLORS (Don't touch guys, ik what im doing)
        self.C_BG = "#0b1220"
        self.C_PANEL = "#111a2c"
        self.C_CARD = "#17233b"
        self.C_ACCENT = "#7c3aed"
        self.C_ACCENT2 = "#06b6d4"
        self.C_TEXT = "#e5e7eb"
        self.C_MUTED = "#9ca3af"
        self.C_GOOD = "#22c55e"
        self.C_BAD = "#ef4444"

        self.root.configure(bg=self.C_BG)

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TFrame", background=self.C_BG)
        self.style.configure("Card.TFrame", background=self.C_CARD)
        self.style.configure("Panel.TFrame", background=self.C_PANEL)
        self.style.configure("TLabel", background=self.C_BG, foreground=self.C_TEXT, font=("Segoe UI", 11))
        self.style.configure("TCombobox", padding=6)

        # Going to load the data using this helper function, better than cluttering __init__, its supposed to be neat
        self.metals, self.salts, self.compound_names, self.compound_list = self._load_dropdown_data()

        # Layout: the left panel and the main content area
        self.nav = ttk.Frame(self.root, style="Panel.TFrame")
        self.nav.pack(side="left", fill="y")

        # Guys i told you this is neater (malaz)
        self.main = ttk.Frame(self.root)
        self.main.pack(side="right", fill="both", expand=True)

        self._build_nav()
        self.frames = {}

        self._build_home()
        self._build_reaction_lab()
        self._build_compound_inspector()
        self._build_organic_generator()
        self._build_history_viewer()

        self.show("home")

    # Data loading helper, has a failsafe so that if for some reason the files arent there,
    # It just makes some basic stuff so the program doesn't crash. (ALSO USES TRY EXCEPT)
    def _load_dropdown_data(self):
        metals = []
        salts = []
        compound_names = []
        compound_list_data = {}

        try:
            from elements import halogen_list
            from elements import activity_series as metals
            from compounds import compound_list as compound_list_data

            new_halogens = []
            for halogen in set(halogen_list):
                new_halogens.append(halogen[0])

            halogens = list(new_halogens)
            salts = sorted({f"{metal}-{halogen}" for metal in metals for halogen in halogens})
            compound_names = sorted(list(compound_list_data.keys()))
        except Exception:
            metals = ["Li", "Na", "K", "Mg", "Ca"]
            salts = [f"{metal}-Cl" for metal in metals]
            compound_names = ["Water", "Sodium Chloride"]
            compound_list_data = {
                "Water": [("H2O"), 3, "Covalent", -285.83],
                "Sodium Chloride": [("NaCl"), 2, "Ionic", -411],
            }

        return metals, salts, compound_names, compound_list_data
    
    # This lets us use backend.react() but the data returned looks prettier ig
    def _react_backend(self, metal: str, salt: str) -> str:
        try:
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
                import backend

            if not hasattr(backend, "react"):
                return "Error: backend.react() not found."

            out = backend.react(metal, salt)
            return str(out)
        except Exception as exception:
            return f"Error: {exception}"
        
    # Those are just history helpers for the ability to create/view/clear history.
    def _history_path(self) -> str:
        return "history.txt"

    def _read_history_text(self) -> str:
        path = self._history_path()
        if not os.path.isfile(path):
            return ""
        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read().strip()
        except Exception:
            return ""

    def _write_history_line(self, line: str):
        path = self._history_path()
        try:
            mode = "a" if os.path.isfile(path) else "w"
            with open(path, mode, encoding="utf-8") as f:
                f.write(line + "\n")
        except Exception:
            # history failure should not crash the UI
            pass

    def _clear_history(self):
        path = self._history_path()
        if not os.path.isfile(path):
            messagebox.showinfo("Clear History", "No history.txt file to clear.")
            self._refresh_history()
            return

        if not messagebox.askyesno("Clear History", "Are you sure you want to clear the history log?"):
            return

        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write("")
            self._refresh_history()
            messagebox.showinfo("Clear History", "History cleared.")
        except Exception as e:
            messagebox.showerror("Clear History", f"Could not clear history: {e}")

    def _refresh_history(self):
        if not hasattr(self, "history_box"):
            return

        content = self._read_history_text()

        # Toggle between empty-state card and text box
        if not content:
            self.history_text_wrap.pack_forget()
            self.history_empty_wrap.pack(fill="both", expand=True)
            return

        self.history_empty_wrap.pack_forget()
        self.history_text_wrap.pack(fill="both", expand=True)

        self.history_box.configure(state="normal")
        self.history_box.delete("1.0", "end")
        self.history_box.insert("1.0", content + "\n")
        self.history_box.configure(state="disabled")

    # NOW, we build the GUI :))))
    def _build_nav(self):
        header = tk.Frame(self.nav, bg=self.C_PANEL)
        header.pack(fill="x", padx=14, pady=16)

        tk.Label(header, text="CURIOUS\nCHEMISTS", bg=self.C_PANEL, fg=self.C_TEXT,
                 font=("Segoe UI", 18, "bold"), justify="left").pack(anchor="w")
        tk.Label(header, text="CuriousChemists UI", bg=self.C_PANEL, fg=self.C_MUTED,
                 font=("Segoe UI", 10)).pack(anchor="w", pady=(6, 0))

        self._nav_btn("Home", lambda: self.show("home"))
        self._nav_btn("Reaction Lab", lambda: self.show("react"))
        self._nav_btn("Compound Inspector", lambda: self.show("inspect"))
        self._nav_btn("Organic Generator", lambda: self.show("organic"))
        self._nav_btn("Log / History", lambda: self.show("history"))

        ttk.Separator(self.nav, orient="horizontal").pack(fill="x", padx=14, pady=12)
        self._nav_btn("Quit", self.root.destroy, danger=True)

    def _nav_btn(self, text, cmd, danger=False):
        button = tk.Button(self.nav,
                           text=text,
                           command=cmd,
                           bg=("#1f2937" if not danger else "#3b1f1f"),
                           fg=self.C_TEXT,
                           activebackground=(self.C_ACCENT2 if not danger else self.C_BAD),
                           activeforeground=("#07101a"),
                           relief="flat",
                           font=("Segoe UI", 11, "bold"),
                           padx=12, pady=10,
                           anchor="w")
        button.pack(fill="x", padx=14, pady=6)

    def _build_home(self):
        frame = ttk.Frame(self.main)
        self.frames["home"] = frame

        tk.Label(frame, text="CuriousChemists", bg=self.C_BG, fg=self.C_TEXT,
                 font=("Segoe UI", 24, "bold")).pack(anchor="w", padx=24, pady=(26, 8))
        tk.Label(frame, text="Use the menu on the left to explore tools.",
                 bg=self.C_BG, fg=self.C_MUTED, font=("Segoe UI", 12)).pack(anchor="w", padx=24)

        card = ttk.Frame(frame, style="Card.TFrame")
        card.pack(fill="x", padx=24, pady=24)

        tk.Label(card, text="Quick Start", bg=self.C_CARD, fg=self.C_TEXT,
                 font=("Segoe UI", 14, "bold")).pack(anchor="w", padx=18, pady=(14, 6))
        tk.Label(card, text="Try Reaction Lab, Compound Inspector, or Organic Generator.\n"
                            "Logs are saved to history.txt.",
                 bg=self.C_CARD, fg=self.C_MUTED, font=("Segoe UI", 11), justify="left").pack(anchor="w", padx=18, pady=(0, 14))

    def _build_reaction_lab(self):
        frame = ttk.Frame(self.main)
        self.frames["react"] = frame

        tk.Label(frame, text="Reaction Lab", bg=self.C_BG, fg=self.C_TEXT,
                 font=("Segoe UI", 22, "bold")).pack(anchor="w", padx=24, pady=(22, 6))

        card = ttk.Frame(frame, style="Card.TFrame")
        card.pack(fill="both", expand=True, padx=24, pady=18)

        row = tk.Frame(card, bg=self.C_CARD)
        row.pack(fill="x", padx=18, pady=(16, 10))

        tk.Label(row, text="Metal:", bg=self.C_CARD, fg=self.C_TEXT, font=("Segoe UI", 11, "bold")).pack(side="left")
        self.metal_var = tk.StringVar(value=self.metals[0] if self.metals else "")
        ttk.Combobox(row, textvariable=self.metal_var, values=self.metals, state="readonly", width=10).pack(side="left", padx=(10, 18))

        tk.Label(row, text="Salt:", bg=self.C_CARD, fg=self.C_TEXT, font=("Segoe UI", 11, "bold")).pack(side="left")
        self.salt_var = tk.StringVar(value=self.salts[0] if self.salts else "")
        ttk.Combobox(row, textvariable=self.salt_var, values=self.salts, state="readonly", width=18).pack(side="left", padx=(10, 18))

        tk.Button(row, text="REACT", command=self._on_react,
                  bg=self.C_ACCENT, fg="white",
                  activebackground=self.C_ACCENT2,
                  activeforeground="#07101a",
                  relief="flat",
                  font=("Segoe UI", 11, "bold"),
                  padx=18, pady=8).pack(side="right")

        out_wrap = tk.Frame(card, bg=self.C_CARD)
        out_wrap.pack(fill="both", expand=True, padx=18, pady=(6, 18))

        tk.Label(out_wrap, text="Result:", bg=self.C_CARD, fg=self.C_TEXT, font=("Segoe UI", 12, "bold")).pack(anchor="w")

        self.out_box = tk.Text(out_wrap, height=10, wrap="word",
                               bg="#0f172a", fg=self.C_TEXT,
                               insertbackground=self.C_TEXT,
                               relief="flat",
                               font=("Consolas", 11))
        self.out_box.pack(fill="both", expand=True, pady=(8, 0))
        self.out_box.insert("1.0", "Choose inputs and click REACT.\n")
        self.out_box.configure(state="disabled")

    def _build_compound_inspector(self):
        frame = ttk.Frame(self.main)
        self.frames["inspect"] = frame

        tk.Label(frame, text="Compound Inspector", bg=self.C_BG, fg=self.C_TEXT,
                 font=("Segoe UI", 22, "bold")).pack(anchor="w", padx=24, pady=(22, 6))
        tk.Label(frame, text="Select a compound and view its properties.",
                 bg=self.C_BG, fg=self.C_MUTED, font=("Segoe UI", 11)).pack(anchor="w", padx=24, pady=(0, 14))

        card = ttk.Frame(frame, style="Card.TFrame")
        card.pack(fill="both", expand=True, padx=24, pady=18)

        row = tk.Frame(card, bg=self.C_CARD)
        row.pack(fill="x", padx=18, pady=(16, 10))

        tk.Label(row, text="Compound:", bg=self.C_CARD, fg=self.C_TEXT,
                 font=("Segoe UI", 11, "bold")).pack(side="left")

        self.compound_var = tk.StringVar(value=self.compound_names[0] if self.compound_names else "")
        ttk.Combobox(row, textvariable=self.compound_var,
                     values=self.compound_names, state="readonly", width=28).pack(side="left", padx=(10, 18))

        tk.Button(row, text="INSPECT", command=self._on_inspect_compound,
                  bg=self.C_ACCENT, fg="white",
                  activebackground=self.C_ACCENT2,
                  activeforeground="#07101a",
                  relief="flat",
                  font=("Segoe UI", 11, "bold"),
                  padx=18, pady=8).pack(side="right")

        out_wrap = tk.Frame(card, bg=self.C_CARD)
        out_wrap.pack(fill="both", expand=True, padx=18, pady=(6, 18))

        tk.Label(out_wrap, text="Properties:", bg=self.C_CARD, fg=self.C_TEXT,
                 font=("Segoe UI", 12, "bold")).pack(anchor="w")

        self.inspect_box = tk.Text(out_wrap, height=12, wrap="word",
                                   bg="#0f172a", fg=self.C_TEXT,
                                   insertbackground=self.C_TEXT,
                                   relief="flat",
                                   font=("Consolas", 11))
        self.inspect_box.pack(fill="both", expand=True, pady=(8, 0))
        self.inspect_box.insert("1.0", "Select a compound and click INSPECT.\n")
        self.inspect_box.configure(state="disabled")

    def _build_organic_generator(self):
        """
        GUI version of organic_compound_generator.py:
        - Same prefix dictionary
        - Same formula logic (alkane/ene/yne)
        - Same history write format: "User created <name> (<formula>) - <timestamp>"
        """
        frame = ttk.Frame(self.main)
        self.frames["organic"] = frame

        tk.Label(frame, text="Organic Compound Generator", bg=self.C_BG, fg=self.C_TEXT,
                 font=("Segoe UI", 22, "bold")).pack(anchor="w", padx=24, pady=(22, 6))
        tk.Label(frame, text="Generate a simple hydrocarbon name + formula.",
                 bg=self.C_BG, fg=self.C_MUTED, font=("Segoe UI", 11)).pack(anchor="w", padx=24, pady=(0, 14))

        card = ttk.Frame(frame, style="Card.TFrame")
        card.pack(fill="both", expand=True, padx=24, pady=18)

        row = tk.Frame(card, bg=self.C_CARD)
        row.pack(fill="x", padx=18, pady=(16, 10))

        tk.Label(row, text="Type:", bg=self.C_CARD, fg=self.C_TEXT, font=("Segoe UI", 11, "bold")).pack(side="left")

        self.org_type_var = tk.StringVar(value="Alkane")
        ttk.Combobox(
            row,
            textvariable=self.org_type_var,
            values=["Alkane", "Alkene", "Alkyne"],
            state="readonly",
            width=12
        ).pack(side="left", padx=(10, 18))

        tk.Label(row, text="Carbons:", bg=self.C_CARD, fg=self.C_TEXT, font=("Segoe UI", 11, "bold")).pack(side="left")

        self.org_carbons_var = tk.IntVar(value=1)
        ttk.Combobox(
            row,
            textvariable=self.org_carbons_var,
            values=list(range(1, 11)),
            state="readonly",
            width=6
        ).pack(side="left", padx=(10, 18))

        tk.Button(row, text="GENERATE", command=self._on_generate_organic,
                  bg=self.C_ACCENT, fg="white",
                  activebackground=self.C_ACCENT2,
                  activeforeground="#07101a",
                  relief="flat",
                  font=("Segoe UI", 11, "bold"),
                  padx=18, pady=8).pack(side="right")

        out_wrap = tk.Frame(card, bg=self.C_CARD)
        out_wrap.pack(fill="both", expand=True, padx=18, pady=(6, 18))

        tk.Label(out_wrap, text="Output:", bg=self.C_CARD, fg=self.C_TEXT,
                 font=("Segoe UI", 12, "bold")).pack(anchor="w")

        self.org_box = tk.Text(out_wrap, height=10, wrap="word",
                               bg="#0f172a", fg=self.C_TEXT,
                               insertbackground=self.C_TEXT,
                               relief="flat",
                               font=("Consolas", 11))
        self.org_box.pack(fill="both", expand=True, pady=(8, 0))
        self.org_box.insert("1.0", "Pick a type + carbon count, then click GENERATE.\n")
        self.org_box.configure(state="disabled")

    def _build_history_viewer(self):
        frame = ttk.Frame(self.main)
        self.frames["history"] = frame

        tk.Label(frame, text="Log / History", bg=self.C_BG, fg=self.C_TEXT,
                 font=("Segoe UI", 22, "bold")).pack(anchor="w", padx=24, pady=(22, 6))
        tk.Label(frame, text="View actions recorded in history.txt (react/inspect/generator events).",
                 bg=self.C_BG, fg=self.C_MUTED, font=("Segoe UI", 11)).pack(anchor="w", padx=24, pady=(0, 14))

        card = ttk.Frame(frame, style="Card.TFrame")
        card.pack(fill="both", expand=True, padx=24, pady=18)

        row = tk.Frame(card, bg=self.C_CARD)
        row.pack(fill="x", padx=18, pady=(16, 10))

        tk.Button(row, text="REFRESH", command=self._refresh_history,
                  bg=self.C_ACCENT, fg="white",
                  activebackground=self.C_ACCENT2,
                  activeforeground="#07101a",
                  relief="flat",
                  font=("Segoe UI", 11, "bold"),
                  padx=18, pady=8).pack(side="right", padx=(10, 0))

        tk.Button(row, text="CLEAR", command=self._clear_history,
                  bg="#3b1f1f", fg="white",
                  activebackground=self.C_BAD,
                  activeforeground="#07101a",
                  relief="flat",
                  font=("Segoe UI", 11, "bold"),
                  padx=18, pady=8).pack(side="right")

        # container for either empty-state or the real text viewer
        self.history_body = tk.Frame(card, bg=self.C_CARD)
        self.history_body.pack(fill="both", expand=True, padx=18, pady=(6, 18))

        # Empty state
        self.history_empty_wrap = tk.Frame(self.history_body, bg=self.C_CARD)
        empty_card = tk.Frame(self.history_empty_wrap, bg="#0f172a", bd=0, highlightthickness=0)
        empty_card.pack(expand=True)

        tk.Label(empty_card, text="No history yet", bg="#0f172a", fg=self.C_TEXT,
                 font=("Segoe UI", 16, "bold")).pack(padx=30, pady=(24, 6))
        tk.Label(empty_card, text="Run a reaction, inspect a compound, or generate an organic compound.\n"
                                  "Your activity will appear here.",
                 bg="#0f172a", fg=self.C_MUTED, font=("Segoe UI", 11), justify="center").pack(padx=30, pady=(0, 24))

        # Text viewer
        self.history_text_wrap = tk.Frame(self.history_body, bg=self.C_CARD)

        self.history_box = tk.Text(self.history_text_wrap, height=14, wrap="word",
                                   bg="#0f172a", fg=self.C_TEXT,
                                   insertbackground=self.C_TEXT,
                                   relief="flat",
                                   font=("Consolas", 10))
        self.history_box.pack(fill="both", expand=True)
        self.history_box.configure(state="disabled")

        # initialize state
        self._refresh_history()

    # Those are action helpers, gl w making the docstrings lol
    def _on_react(self):
        metal = (self.metal_var.get() or "").strip()
        salt = (self.salt_var.get() or "").strip()

        if not metal or not salt:
            messagebox.showwarning("Missing input", "Please select both a metal and a salt.")
            return
        if "-" not in salt:
            messagebox.showwarning("Invalid salt", "Salt should look like 'Na-Cl'.")
            return

        result = self._react_backend(metal, salt)

        self.out_box.configure(state="normal")
        self.out_box.delete("1.0", "end")
        self.out_box.insert("1.0", f"Inputs:\n  Metal = {metal}\n  Salt  = {salt}\n\nOutput:\n  {result}\n")
        self.out_box.configure(state="disabled")

    def _on_inspect_compound(self):
        name = (self.compound_var.get() or "").strip()
        if not name:
            messagebox.showwarning("Missing input", "Please select a compound.")
            return
        if name not in self.compound_list:
            messagebox.showwarning("Unknown compound", "That compound is not in the list.")
            return

        props = self.compound_list[name]
        lines = [
            f"Compound: {name}",
            f"Chemical Formula: {props[0]}",
            f"Total number of atoms: {props[1]}",
            f"Compound Type: {props[2]}",
            f"Enthalpy of Formation: {props[3]}",
        ]

        # keep same style as your other modules
        dt_string = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        self._write_history_line(f"User inspected {name} - {dt_string}")

        self.inspect_box.configure(state="normal")
        self.inspect_box.delete("1.0", "end")
        self.inspect_box.insert("1.0", "\n".join(lines) + "\n")
        self.inspect_box.configure(state="disabled")

    def _on_generate_organic(self):
        # Matches the logic in organic_compound_generator.py :contentReference[oaicite:2]{index=2}
        prefix_dictionary = {
            1: "Meth", 2: "Eth", 3: "Prop", 4: "But", 5: "Pent",
            6: "Hex", 7: "Hept", 8: "Oct", 9: "Non", 10: "Dec"
        }

        compound_type = (self.org_type_var.get() or "").strip()
        n = int(self.org_carbons_var.get())

        if n < 1 or n > 10:
            messagebox.showwarning("Invalid input", "Carbon chain length must be 1–10.")
            return

        if compound_type == "Alkane":
            formula = f"C{n}H{(2 * n) + 2}"
            name = f"{prefix_dictionary[n]}ane"
        elif compound_type == "Alkene":
            formula = f"C{n}H{(2 * n)}"
            name = f"{prefix_dictionary[n]}ene"
        elif compound_type == "Alkyne":
            formula = f"C{n}H{(2 * n) - 2}"
            name = f"{prefix_dictionary[n]}yne"
        else:
            messagebox.showwarning("Invalid input", "Please select Alkane / Alkene / Alkyne.")
            return

        dt_string = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        # EXACT format from your generator file :contentReference[oaicite:3]{index=3}
        self._write_history_line(f"User created {name} ({formula}) - {dt_string}")

        self.org_box.configure(state="normal")
        self.org_box.delete("1.0", "end")
        self.org_box.insert("1.0", f"Generated:\n  Name:    {name}\n  Formula: {formula}\n")
        self.org_box.configure(state="disabled")

        # If history view is open, refresh it
        if self._current_frame_name == "history":
            self._refresh_history()

    # Final window code so the frame is created and shown.
    def show(self, name: str):
        self._current_frame_name = name
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[name].pack(fill="both", expand=True)

        if name == "history":
            self._refresh_history()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = GUI()
    app.run()