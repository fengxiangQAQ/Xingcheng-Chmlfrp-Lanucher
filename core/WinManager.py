import customtkinter as ctk
import win32gui
import tkinter

import core.g_var as g_var

class MoveWin:

    winx=0
    winy=0

    # 处理鼠标按下事件
    @classmethod
    def on_drag_start(cls,event:tkinter.Event):
        # 识别按下位置
        if str(event.widget)==".!maintabview" or str(event.widget)==".!maintabview.!ctkcanvas" or str(event.widget)==".!ctklabel.!label":
            cls.winx=event.x
            cls.winy=event.y

    # 处理鼠标移动事件
    @classmethod
    def on_drag(cls,event:tkinter.Event):
        if cls.winy!=0:
            deltax=event.x-cls.winx
            deltay=event.y-cls.winy
            new_x=g_var.gui.main_win.winfo_x()+deltax
            new_y=g_var.gui.main_win.winfo_y()+deltay
            g_var.gui.main_win.geometry(f"+{new_x}+{new_y}")
            g_var.gui.cover_stack[0].geometry(f"+{new_x}+{new_y}")
            g_var.gui.cover_stack[1].geometry(f"+{new_x}+{new_y}")
            g_var.gui.cover_stack[2].geometry(f"+{new_x}+{new_y}")
            g_var.gui.cover_stack[3].geometry(f"+{new_x}+{new_y}")

    # 处理鼠标释放事件
    @classmethod
    def on_drag_stop(cls,event:tkinter.Event):
        cls.winx=0
        cls.winy=0
        g_var.gui.cover_stack[0].attributes('-topmost', 'false')
        g_var.gui.cover_stack[1].attributes('-topmost', 'false')
        g_var.gui.cover_stack[2].attributes('-topmost', 'false')
        g_var.gui.cover_stack[3].attributes('-topmost', 'false')

def top_win(event:tkinter.Event): 
    for win in g_var.gui.cover_stack[::-1]:
        win.attributes('-topmost', 'true')
    g_var.gui.main_win.attributes('-topmost', 'true')
    g_var.gui.main_win.attributes('-topmost', 'false')
    for win in g_var.gui.cover_stack:
        win.attributes('-topmost', 'false')

def addTip(tipFrame:ctk.CTkFrame):
    tipFrame.pack(anchor="center",pady=(3,1))