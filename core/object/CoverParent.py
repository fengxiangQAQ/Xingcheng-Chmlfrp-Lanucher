import win32gui
import customtkinter as ctk

class CoverParent(ctk.CTkToplevel):
    CoverFrame:ctk.CTkFrame
    def __init__(self, *args, fg_color = None, **kwargs):
        self.hwnd=win32gui.FindWindow(None, self.title())
        super().__init__(*args, fg_color=fg_color, **kwargs)
