import customtkinter as ctk
import core.g_var

from typing import Callable

from core.object.gui.widgets.PopWin import PopWin
from core.object.gui.widgets.CTkFrameG import CTkFrameG

class ConfirmPopWin(PopWin):

    def __init__(self, master,text:str,callbackFun:Callable[[bool],None],confirmText:str="确认"):
        super().__init__(master)
        main=ConfirmMain(self,text,callbackFun,confirmText)
        main.place(x=0,y=0)
        self.update_idletasks()
        main.place(x=(783-main.winfo_width())/2,y=(418-main.winfo_height())/2)

class ConfirmMain(CTkFrameG):
    def __init__(self,master:ConfirmPopWin,text:str,callbackFun:Callable[[bool],None],confirmText:str):
        super().__init__(master=master,AA=False)
        self.callbackFun=callbackFun
        self.master:ConfirmPopWin=master
        ctk.CTkLabel(self,text="提示",font=("微软雅黑",20,"bold")).grid(row=0,column=0,padx=15,pady=10,sticky="nw")
        ctk.CTkLabel(self,text=text).grid(row=1,column=0,columnspan=2,padx=30)
        ButtonFrame=ctk.CTkFrame(self)
        ButtonFrame.grid(row=2,column=1,padx=7,pady=10,sticky="e")
        ctk.CTkButton(ButtonFrame,text="取消",command=self.cancel,border_width=1.5,border_color="#C5C5D1",text_color="#000000",fg_color="gray90",hover_color="gray87",width=0).grid(row=0,column=0,padx=5)
        ctk.CTkButton(ButtonFrame,text=confirmText,command=self.confirm,width=0).grid(row=0,column=1,padx=5)

    def confirm(self):
        self.callbackFun(True)
        core.g_var.gui.cover_stack[2].setCoverFrame(ctk.CTkFrame(core.g_var.gui.cover_stack[2],fg_color="#0000ff"))

    def cancel(self):
        self.callbackFun(False)
        core.g_var.gui.cover_stack[2].setCoverFrame(ctk.CTkFrame(core.g_var.gui.cover_stack[2],fg_color="#0000ff"))