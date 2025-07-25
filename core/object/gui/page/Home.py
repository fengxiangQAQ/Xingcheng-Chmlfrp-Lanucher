import customtkinter as ctk
import core.g_var

from PIL import Image
from core.object.gui.widgets.PanelButton import PanelRButton
from core.object.gui.widgets.UpMenuButton import upMenuButton

class homeFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,width=783,height=418,corner_radius=0,fg_color="#0000ff")
        sidebarFrame(self).place(x=0,y=0)
        upMenuButton(self,"启动！\n你选隧道了吗?").place(x=585,y=350)

class sidebarFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,height=418,width=225,corner_radius=0)
        self.pack_propagate(0)
        ctk.CTkLabel(self,text="",image=ctk.CTkImage(light_image=Image.open("./XCL/userimg.png").resize((70,70)),size=(70,70))).pack(pady=(15,0))
        self.name=ctk.CTkFrame(self)
        self.name.pack()
        ctk.CTkLabel(self.name,text=core.g_var.User.basicInfo["username"],font=("微软雅黑",16)).pack(side="left")
        ctk.CTkLabel(self.name,text=f"#{core.g_var.User.id}",font=("微软雅黑",16),text_color="#808080").pack(side="left",padx=3)
        userInfoFrame(self).pack(pady=(16,0))
        # TODO重置token
        PanelRButton(self,text="重置token").pack(pady=(16,0))

class userInfoFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,corner_radius=0,fg_color="gray84")
        ctk.CTkFrame(self,width=223,height=0).pack()
        ctk.CTkLabel(self,text="权限组："+core.g_var.User.basicInfo["usergroup"],font=("微软雅黑",12)).pack(side="top",anchor=ctk.W,padx=15)
        ctk.CTkLabel(self,text="隧道限制："+str(core.g_var.User.basicInfo["tunnelCount"])+"/"+str(core.g_var.User.basicInfo["tunnel"]),font=("微软雅黑",12)).pack(side="top",anchor=ctk.W,padx=15)
        ctk.CTkLabel(self,text="剩余积分："+str(core.g_var.User.basicInfo["integral"]),font=("微软雅黑",12)).pack(side="top",anchor=ctk.W,padx=15)
        ctk.CTkLabel(self,text="带宽限制："+str(core.g_var.User.basicInfo["bandwidth"])+"m/"+str(core.g_var.User.basicInfo["bandwidth"]*4)+"m",font=("微软雅黑",12)).pack(side="top",anchor=ctk.W,padx=15)
        ctk.CTkLabel(self,text="实名状态："+core.g_var.User.basicInfo["realname"],font=("微软雅黑",12)).pack(side="top",anchor=ctk.W,padx=15)
        ctk.CTkLabel(self,text="绑定邮箱："+core.g_var.User.basicInfo["email"],font=("微软雅黑",12)).pack(side="top",anchor=ctk.W,padx=15)