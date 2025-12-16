import time
from tkinter import *

class GUI():
    def __init__(self):
        self.win = Tk()
        self.win.title("CuriousChemists")

    def create_screen(self):
        pass

    def update_screen(self):
        self.win.update()
        time.sleep(1/60)

app = GUI()

while True:
    app.update_screen()