import customtkinter as ctk

import core.g_var
from core.object.gui.widgets.CTkScrollableFrameFrame import CTkScrollableFrameFrame
from core.object.gui.widgets.CTkButtonG import CTkButtonG

class upMenuButton(ctk.CTkFrame):
    def __init__(self,master:ctk.CTkFrame,text:str):
        super().__init__(master,fg_color="#0000ff")
        self.text=text
        self.menuStatus=False
        self.chooseid=None
        self.menuObj:MenuFrame=None
        self.master:ctk.CTkFrame=master
        self.mainButton:ctk.CTkButton=CTkButtonG(self,text=self.text,height=43,noCorner="right",state="disabled",command=self.startFrp,AA=False)
        self.menuButton:ctk.CTkButton=CTkButtonG(self,text="⇧",font=("微软雅黑",20,"bold"),height=43,width=25,fg_color="#48AA9B",noCorner="left",command=self.menuOperation,AA=False)
        self.mainButton.pack(side="left")
        self.menuButton.pack(side="left")
    def menuOperation(self):
        if self.menuStatus:
            self.menuObj.destroy()
            self.menuStatus=False
            self.menuButton.configure(text="⇧")
        else:
            self.menuObj=MenuFrame(self)
            self.menuObj.place(x=self.winfo_x()+13,y=self.winfo_y()-163)
            self.menuStatus=True
            self.menuButton.configure(text="⇩")
    def startFrp(self):
        pass
        #startFrpc(self.chooseid)

class MenuFrame(CTkScrollableFrameFrame):
    def __init__(self,master:upMenuButton):
        self.smaster=master
        super().__init__(core.g_var.gui.main_win,width=142)
        for options in core.g_var.User.TunnelDict.keys():
            Options(self.ScrollableFrame,self,core.g_var.User.TunnelDict[options]).pack(anchor=ctk.W,pady=3)

class Options(ctk.CTkButton):
    def __init__(self,master,rmaster:MenuFrame,data:dict):
        self.smaster=rmaster
        self.id=data["id"]
        self.name=data["name"]
        self.text=f"#{self.id} {self.name}"
        super().__init__(master,text=self.text,height=32,command=self.cs)
    def cs(self):
        self.smaster.smaster.menuOperation()
        self.smaster.smaster.chooseid=self.id
        self.smaster.smaster.mainButton.configure(text=f"启动！\n{self.text}",state="normal")