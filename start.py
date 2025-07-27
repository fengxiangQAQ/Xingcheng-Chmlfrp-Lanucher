import os
import json
import urllib.request
import customtkinter as ctk
import core.g_var

from core.g_var import gui
from core.object.gui.MainWin import Main

def init():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("./res/xcTheme.json")
    if not os.path.isdir("./XCL"):
        os.mkdir("./XCL")
    if not os.path.isfile("./XCL/config.json"):
        with open("./XCL/config.json","w") as file:
            file.write('{\"bg_path\":\"./res/bg.jpg\"}')
    core.g_var.lanucherConfig=json.loads(open("./XCL/config.json","r").read())
    urllib.request.install_opener(urllib.request.build_opener(
        urllib.request.ProxyHandler({})  # 禁用代理
    )) 

if __name__ == "__main__":
    init()
    gui.main_win=Main()
    gui.main_win.mainloop()
