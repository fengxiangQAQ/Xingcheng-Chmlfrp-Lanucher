import win32gui
import win32con
import win32api
import customtkinter as ctk

import core.g_var as g_var

class CoverWin(ctk.CTkToplevel):
    def __init__(self, *args, fg_color = None, **kwargs):
        super().__init__(g_var.gui.main_win,*args, fg_color=fg_color, **kwargs)
        self.CoverFrame:ctk.CTkFrame=ctk.CTkFrame(self)
        self.geometry("783x418")
        self.overrideredirect(True)
        self.hwnd = win32gui.GetParent(self.winfo_id())
        # 启用分层样式
        win32gui.SetWindowLong(
            self.hwnd,
            win32con.GWL_EXSTYLE,
            win32gui.GetWindowLong(self.hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED
        )
        win32gui.SetLayeredWindowAttributes(self.hwnd, win32api.RGB(*(0,0,255)), 218, win32con.LWA_ALPHA | win32con.LWA_COLORKEY)
        self.update_idletasks()
    
    def setCoverFrame(self,newFrame:ctk.CTkFrame):
        self.CoverFrame.destroy()
        self.CoverFrame=newFrame
        self.CoverFrame.place(x=0,y=0)
        self.update_idletasks()
