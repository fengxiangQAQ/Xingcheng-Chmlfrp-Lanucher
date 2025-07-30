import win32gui
import win32con
import win32api
import win32process
import customtkinter as ctk

import core.g_var as g_var

from core.object.gui.widgets.MainTabView import MainTabView
from core.object.gui.widgets.CTkButtonG import CTkButtonG
from core.object.gui.CoverWin import CoverWin
from core.object.gui.page import Mask
from core.WinManager import MoveWin,top_win

class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("XingCheng Chmlfrp Lanucher - main")
        self.geometry("810x480")
        self.wm_attributes('-transparentcolor','#0000ff')
        self.main_tab_view=MainTabView(master=self)
        self.main_tab_view.place(x=0,y=0)
        self.close_win_button=CTkButtonG(self,text="x",width=42,height=42,font=("微软雅黑",23,"bold"),corner_radius=15,command=self.destroy,fg_color="#ebebeb",hover_color="#e1e1e1",text_color="#bebebe")
        self.close_win_button.place(relx=0.92,y=5)
        ctk.CTkLabel(self,text="XCL  II",font=("微软雅黑",22,"bold")).place(x=30,y=10)
        # 遮盖背景
        self.shelter_down=ctk.CTkLabel(self,text="",width=810,height=13,bg_color="#0000FF")
        self.shelter_down.place(x=0,y=467)
        self.shelter_left=ctk.CTkLabel(self,text="",width=13,height=480,bg_color="#0000FF")
        self.shelter_left.place(x=0,y=0)
        self.shelter_right=ctk.CTkLabel(self,text="",width=13,height=480,bg_color="#0000FF")
        self.shelter_right.place(x=797,y=0)
        self.bind("<ButtonPress-1>",MoveWin.on_drag_start)
        self.bind("<B1-Motion>",MoveWin.on_drag)
        self.bind("<ButtonRelease-1>",MoveWin.on_drag_stop)
        self.main_tab_view.add_tab("登录")
        self.main_tab_view.add_tab("设置")
        # 无边框
        self.overrideredirect(True)
        self.hwnd = win32gui.GetParent(self.winfo_id())
        extended_style = win32gui.GetWindowLong(self.hwnd, win32con.GWL_EXSTYLE)
        win32gui.SetWindowLong(self.hwnd, win32con.GWL_EXSTYLE, extended_style | win32con.WS_EX_APPWINDOW)
        win32gui.SetWindowPos(self.hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_FRAMECHANGED)
        # -
        self.update_idletasks()
        self.attributes('-topmost', 'true')
        self.attributes('-topmost', 'false')
        g_var.gui.cover_stack.append(CoverWin())
        g_var.gui.cover_stack.append(CoverWin(WINalpha=66))
        g_var.gui.cover_stack.append(CoverWin(WINalpha=255))
        g_var.gui.cover_stack.append(CoverWin(WINalpha=235))
        g_var.gui.cover_stack[0].geometry(f"+{self.winfo_x()}+{self.winfo_x()}")
        g_var.gui.cover_stack[1].geometry(f"+{self.winfo_x()}+{self.winfo_x()}")
        g_var.gui.cover_stack[2].geometry(f"+{self.winfo_x()}+{self.winfo_x()}")
        g_var.gui.cover_stack[3].geometry(f"+{self.winfo_x()}+{self.winfo_x()}")
        g_var.gui.mask=Mask.MaskFrame(g_var.gui.cover_stack[1])
        g_var.gui.cover_stack[1].setCoverFrame(g_var.gui.mask)
        g_var.gui.cover_stack[3].setCoverFrame(ctk.CTkFrame(g_var.gui.cover_stack[3],width=784,height=418,corner_radius=0,fg_color="#0000ff"))
        g_var.gui.cover_stack[3].CoverFrame.pack_propagate(False)
        self.main_tab_view.upTabCoverWin()

    # Override
    def mainloop(self, *args, **kwargs):
        self.check_topmost()
        super().mainloop(*args, **kwargs)

    # Override
    def destroy(self):
        # 获取进程ID
        _, pid = win32process.GetWindowThreadProcessId(self.hwnd)
        
        # 打开进程
        handle = win32api.OpenProcess(win32con.PROCESS_TERMINATE, 0, pid)
        
        # 终止进程
        win32api.TerminateProcess(handle, 0)
        win32api.CloseHandle(handle)

    def check_topmost(self):
        try:
            # 获取当前最上面的窗口句柄
            top_window = win32gui.GetForegroundWindow()
            if top_window == self.hwnd:
                top_win(None)
        except:
            pass
        # 继续循环检查
        self.after(30, self.check_topmost)
