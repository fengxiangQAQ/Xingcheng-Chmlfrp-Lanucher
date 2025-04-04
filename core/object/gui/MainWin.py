import win32gui
import win32con
import customtkinter as ctk

import core.g_var as g_var

from core.object.gui.widgets.MainTabView import MainTabView
from core.object.gui.widgets.CTkButtonG import CTkButtonG

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
        # Login 窗口处理
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

class MoveWin:

    winx=0
    winy=0

    # 处理鼠标按下事件
    def on_drag_start(event):
        # 识别按下位置
        if str(event.widget)==".!maintabview" or str(event.widget)==".!maintabview.!ctkcanvas" or str(event.widget)==".!ctklabel.!label":
            MoveWin.winx=event.x
            MoveWin.winy=event.y

    # 处理鼠标移动事件
    def on_drag(event):
        if MoveWin.winy!=0:
            deltax=event.x-MoveWin.winx
            deltay=event.y-MoveWin.winy
            new_x=g_var.gui.main_win.winfo_x()+deltax
            new_y=g_var.gui.main_win.winfo_y()+deltay
            g_var.gui.main_win.geometry(f"+{new_x}+{new_y}")

    # 处理鼠标释放事件
    def on_drag_stop(event):
        MoveWin.winx=0
        MoveWin.winy=0