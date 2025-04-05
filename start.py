import customtkinter as ctk

from core.g_var import gui
from core.object.gui.MainWin import Main

def init():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("./res/xcTheme.json")

if __name__ == "__main__":
    init()
    gui.main_win=Main()
    gui.main_win.mainloop()
