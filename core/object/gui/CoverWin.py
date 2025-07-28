import win32gui
import win32con
import win32api
import customtkinter as ctk

import core.g_var as g_var
from core.WinManager import top_win

class CoverWin(ctk.CTkToplevel):
    def __init__(self,WINalpha:int=218,*args, fg_color = None, **kwargs):
        super().__init__(g_var.gui.main_win,*args, fg_color="#0000ff", **kwargs)
        self.CoverFrame:ctk.CTkFrame=ctk.CTkFrame(self)
        self.geometry("810x480")
        self.overrideredirect(True)
        self.bind("<ButtonPress-1>",top_win)
        self.hwnd = win32gui.GetParent(self.winfo_id())
        # 启用分层样式
        win32gui.SetWindowLong(
            self.hwnd,
            win32con.GWL_EXSTYLE,
            win32gui.GetWindowLong(self.hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED
        )
        win32gui.SetLayeredWindowAttributes(self.hwnd, win32api.RGB(*(0,0,255)), WINalpha, win32con.LWA_ALPHA | win32con.LWA_COLORKEY)
        self.update_idletasks()
    
    def setCoverFrame(self,newFrame:ctk.CTkFrame):
        self.CoverFrame.destroy()
        self.CoverFrame=newFrame
        self.CoverFrame.place(x=13,y=49)
        self.update_idletasks()
