import os
import urllib.request
import customtkinter as ctk

from core.g_var import gui
from core.object.gui.MainWin import Main

def init():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("./res/xcTheme.json")
    if not os.path.isdir("./XCL"):
        os.mkdir("./XCL")
    urllib.request.install_opener(urllib.request.build_opener(
        urllib.request.ProxyHandler({})  # 禁用代理
    )) 

if __name__ == "__main__":
    init()
    gui.main_win=Main()
    gui.main_win.mainloop()
