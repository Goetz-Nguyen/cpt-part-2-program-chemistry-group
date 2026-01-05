# menu.py
import tkinter as tk
from tkinter import ttk, messagebox
import contextlib
import io

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CuriousChemists")
        self.root.geometry("900x560")
        self.root.minsize(820, 520)

        # --- Theme colors (simple, colorful) ---
        self.C_BG = "#0b1220"       # deep navy
        self.C_PANEL = "#111a2c"    # panel navy
        self.C_CARD = "#17233b"     # card
        self.C_ACCENT = "#7c3aed"   # purple
        self.C_ACCENT2 = "#06b6d4"  # cyan
        self.C_TEXT = "#e5e7eb"     # near-white
        self.C_MUTED = "#9ca3af"    # gray
        self.C_GOOD = "#22c55e"     # green
        self.C_BAD = "#ef4444"      # red

        self.root.configure(bg=self.C_BG)

        # Use ttk but style it a bit
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure("TFrame", background=self.C_BG)
        self.style.configure("Card.TFrame", background=self.C_CARD)
        self.style.configure("Panel.TFrame", background=self.C_PANEL)

        self.style.configure("TLabel", background=self.C_BG, foreground=self.C_TEXT, font=("Segoe UI", 11))
        self.style.configure("Title.TLabel", background=self.C_BG, foreground=self.C_TEXT, font=("Segoe UI", 20, "bold"))
        self.style.configure("Sub.TLabel", background=self.C_BG, foreground=self.C_MUTED, font=("Segoe UI", 11))

        self.style.configure("TButton", font=("Segoe UI", 11, "bold"), padding=10)
        self.style.map("TButton",
                       background=[("active", self.C_ACCENT2), ("!active", self.C_ACCENT)],
                       foreground=[("active", "#07101a"), ("!active", "white")])

        self.style.configure("TCombobox", padding=6)

        # --- Load data safely (local imports inside method) ---
        self.metals, self.salts = self._load_dropdown_data()

        # --- Layout: left nav + main content ---
        self.nav = ttk.Frame(self.root, style="Panel.TFrame")
        self.nav.pack(side="left", fill="y")

        self.main = ttk.Frame(self.root)
        self.main.pack(side="right", fill="both", expand=True)

        self._build_nav()
        self.frames = {}
        self._build_home()
        self._build_reaction_lab()
        self.show("home")

    # ----------------- Data Loading -----------------
    def _load_dropdown_data(self):
        """
        Builds metal + salt lists from the project modules.
        Anti-crash: falls back to small defaults if something fails.
        """
        metals = []
        salts = []

        try:
            # local imports
            from elements import alkali_metal_list, alkaline_earth_metal_list, halogen_list, activity_series

            new_metals = []
            new_halogens = []

            for e in set(alkali_metal_list + alkaline_earth_metal_list):
                new_metals.append(e[0])
            metals = sorted(new_metals)

            # metals = [].append(metal for metal in metals if metal in activity_series)

            for h in set(halogen_list):
                new_halogens.append(h[0])
            
            halogens = list(new_halogens)

            # salts like "Na-Cl"
            salts = sorted({f"{m}-{h}" for m in metals for h in halogens})
        except Exception:
            # fallback (won't crash the UI)
            metals = ["Li", "Na", "K", "Mg", "Ca"]
            salts = [f"{m}-Cl" for m in metals]

        return metals, salts

    # ----------------- Backend Call (Quiet Import) -----------------
    def _react_backend(self, metal: str, salt: str) -> str:
        """
        Calls backend.react(metal, salt) while suppressing any import-time prints.
        """
        try:
            # backend.py currently prints at import-time in the project.
            # This keeps the UI clean.
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
                import backend  # local import, quiet

            # If react exists, call it
            if not hasattr(backend, "react"):
                return "Error: backend.react() not found."
            
            print(salt)
            out = backend.react(metal, salt)
            return str(out)
        except Exception as e:
            return f"Error: {e}"

    # ----------------- UI Building -----------------
    def _build_nav(self):
        # Logo/header
        header = tk.Frame(self.nav, bg=self.C_PANEL)
        header.pack(fill="x", padx=14, pady=16)

        tk.Label(header, text="CURIOUS\nCHEMISTS", bg=self.C_PANEL, fg=self.C_TEXT,
                 font=("Segoe UI", 18, "bold"), justify="left").pack(anchor="w")
        tk.Label(header, text="CuriousChemists UI", bg=self.C_PANEL, fg=self.C_MUTED,
                 font=("Segoe UI", 10)).pack(anchor="w", pady=(6, 0))

        # Buttons
        self._nav_btn("Home", lambda: self.show("home"))
        self._nav_btn("Reaction Lab", lambda: self.show("react"))
        ttk.Separator(self.nav, orient="horizontal").pack(fill="x", padx=14, pady=12)

        # Quit
        self._nav_btn("Quit", self.root.destroy, danger=True)

    def _nav_btn(self, text, cmd, danger=False):
        # simple custom button using tk for color control
        b = tk.Button(self.nav,
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
        b.pack(fill="x", padx=14, pady=6)

    def _build_home(self):
        f = ttk.Frame(self.main)
        self.frames["home"] = f

        # Hero
        tk.Label(f, text="CuriousChemists", bg=self.C_BG, fg=self.C_TEXT,
                 font=("Segoe UI", 24, "bold")).pack(anchor="w", padx=24, pady=(26, 8))
        tk.Label(f, text="Pick a metal and a salt. Click React. That’s it.",
                 bg=self.C_BG, fg=self.C_MUTED, font=("Segoe UI", 12)).pack(anchor="w", padx=24)

        # Card
        card = ttk.Frame(f, style="Card.TFrame")
        card.pack(fill="x", padx=24, pady=24)

        tk.Label(card, text="Quick Start", bg=self.C_CARD, fg=self.C_TEXT,
                 font=("Segoe UI", 14, "bold")).pack(anchor="w", padx=18, pady=(14, 6))
        tk.Label(card, text="Go to Reaction Lab → choose metal + salt → React.",
                 bg=self.C_CARD, fg=self.C_MUTED, font=("Segoe UI", 11)).pack(anchor="w", padx=18, pady=(0, 14))

        # Small footer
        tk.Label(f, text="Note: This UI is minimal (short & sort of stable).",
                 bg=self.C_BG, fg=self.C_MUTED, font=("Segoe UI", 10)).pack(anchor="w", padx=24, pady=(0, 12))

    def _build_reaction_lab(self):
        f = ttk.Frame(self.main)
        self.frames["react"] = f

        tk.Label(f, text="Reaction Lab", bg=self.C_BG, fg=self.C_TEXT,
                 font=("Segoe UI", 22, "bold")).pack(anchor="w", padx=24, pady=(22, 6))
        tk.Label(f, text="Single-replacement-style reaction (based on the backend rules).",
                 bg=self.C_BG, fg=self.C_MUTED, font=("Segoe UI", 11)).pack(anchor="w", padx=24, pady=(0, 14))

        card = ttk.Frame(f, style="Card.TFrame")
        card.pack(fill="both", expand=True, padx=24, pady=18)

        # Inputs row
        row = tk.Frame(card, bg=self.C_CARD)
        row.pack(fill="x", padx=18, pady=(16, 10))

        tk.Label(row, text="Metal:", bg=self.C_CARD, fg=self.C_TEXT, font=("Segoe UI", 11, "bold")).pack(side="left")
        self.metal_var = tk.StringVar(value=self.metals[0] if self.metals else "")
        metal_cb = ttk.Combobox(row, textvariable=self.metal_var, values=self.metals, state="readonly", width=10)
        metal_cb.pack(side="left", padx=(10, 18))

        tk.Label(row, text="Salt:", bg=self.C_CARD, fg=self.C_TEXT, font=("Segoe UI", 11, "bold")).pack(side="left")
        self.salt_var = tk.StringVar(value=self.salts[0] if self.salts else "")
        salt_cb = ttk.Combobox(row, textvariable=self.salt_var, values=self.salts, state="readonly", width=18)
        salt_cb.pack(side="left", padx=(10, 18))

        # React button
        react_btn = tk.Button(row, text="REACT",
                              command=self._on_react,
                              bg=self.C_ACCENT, fg="white",
                              activebackground=self.C_ACCENT2,
                              activeforeground="#07101a",
                              relief="flat",
                              font=("Segoe UI", 11, "bold"),
                              padx=18, pady=8)
        react_btn.pack(side="right")

        # Output area
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

    # ----------------- Actions -----------------
    def _on_react(self):
        metal = (self.metal_var.get() or "").strip()
        salt = (self.salt_var.get() or "").strip()
        print(type(salt))

        # Anti-crash checks
        if not metal or not salt:
            messagebox.showwarning("Missing input", "Please select both a metal and a salt.")
            return
        if "-" not in salt:
            messagebox.showwarning("Invalid salt", "Salt should look like 'Na-Cl'.")
            return

        result = self._react_backend(metal, salt)

        # Display nicely
        self.out_box.configure(state="normal")
        self.out_box.delete("1.0", "end")
        self.out_box.insert("1.0", f"Inputs:\n  Metal = {metal}\n  Salt  = {salt}\n\nOutput:\n  {result}\n")
        self.out_box.configure(state="disabled")

    # ----------------- Navigation -----------------
    def show(self, name: str):
        for fr in self.frames.values():
            fr.pack_forget()
        self.frames[name].pack(fill="both", expand=True)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    GUI().run()
