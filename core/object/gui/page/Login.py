import customtkinter as ctk
import core.g_var as g_var
import json

from io import BytesIO
from PIL import Image
from core.object.User import User
from core.WinManager import addTip
from core.utils.network.requests import request
from core.utils.network.ChmlfrpApi import APIv2
from core.utils.image.AvatarCircler import AvatarCircler
from core.object.gui.widgets.tip import errorTopTip,successTopTip
from core.object.gui.widgets.CTkFrameG import CTkFrameG
from core.object.gui.popWIN.ConfirmPopWin import ConfirmPopWin

class LoginFrame(CTkFrameG):
    def __init__(self,master):
        super().__init__(master,width=785,height=418,corner_radius=0,fg_color="#0000ff",AA=False)
        LoginMain(self).place(x=345/2,y=148/2)
# 783-438=345 418-270=148

class LoginMain(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,width=438,height=270)
        ctk.CTkLabel(self,text="登 录",font=("微软雅黑",30,"bold")).place(x=21,y=16)
        self.input:LoginInput=LoginInput(self)
        self.input.place(x=64,y=81)
        self.login_B:ctk.CTkButton=ctk.CTkButton(self,text="登录",font=("微软雅黑",15),width=260,height=32,command=self.userLogin)
        self.login_B.place(x=85,y=215)
        self.ckb_KeepLogin=ctk.CTkCheckBox(self,text="保持登录",font=("微软雅黑",12.5),checkbox_height=16.5,checkbox_width=16.5)
        self.ckb_KeepLogin.place(x=65,y=185)
        if "user_token" in g_var.lanucherConfig.keys():
            self.token=g_var.lanucherConfig["user_token"]
            self.login_B.configure(text="尝试登录中...",state="disabled")
            self.after(400,self.automaticLogin)

    def automaticLogin(self):
        try:
            data=APIv2.getUserInfo(self.token)
            # TODO 自动下载frpc
            if data is not None:
                g_var.User=User(data)
                img=Image.open(BytesIO(request.get(g_var.User.basicInfo["userimg"]).content))
                AvatarCircler(img).save("./XCL/userimg.png",'PNG')
                self.upLoginAfter()
            else:
                addTip(errorTopTip(g_var.gui.cover_stack[3].CoverFrame,"保持登录:token已失效"))
        except:
            addTip(errorTopTip(g_var.gui.cover_stack[3].CoverFrame,"保持登录:网络请求错误"))
        self.login_B.configure(text="登录",state="normal")

    def userLogin(self):
        self.login_B.configure(text="登录中...",state="disabled")
        data=APIv2.login(self.input.usernameEntry.get(),self.input.passwordEntey.get())
            # TODO 自动下载frpc
        if data is not None:
            g_var.User=User(data)
            img=Image.open(BytesIO(request.get(g_var.User.basicInfo["userimg"]).content))
            AvatarCircler(img).save("./XCL/userimg.png",'PNG')
            if self.ckb_KeepLogin.get()==1:
                g_var.gui.cover_stack[2].setCoverFrame(ConfirmPopWin(g_var.gui.cover_stack[2],"将保存您的token以用于保持登录 您是否同意?\n注 重置token将无法保持登录",confirmText="同意",callbackFun=self.KeepLogin))
            else:
                self.upLoginAfter()
        else:
            addTip(errorTopTip(g_var.gui.cover_stack[3].CoverFrame,"账号密码错误"))
        self.login_B.configure(text="登录",state="normal")

    def KeepLogin(self,b:bool):
        if b:
            g_var.lanucherConfig["user_token"]=g_var.User.token
            with open("./XCL/config.json","w") as file:
                file.write(json.dumps(g_var.lanucherConfig))
        self.upLoginAfter()

    def upLoginAfter(self):
        g_var.gui.main_win.main_tab_view.delete("登录")
        g_var.gui.main_win.main_tab_view.delete("设置")
        g_var.gui.main_win.main_tab_view.add_tab("Home")
        g_var.gui.main_win.main_tab_view.add_tab("隧道管理")
        g_var.gui.main_win.main_tab_view.add_tab("设置")
        g_var.gui.main_win.main_tab_view.set("Home")
        g_var.User.updateTunnel()
        g_var.gui.main_win.main_tab_view.upTabCoverWin()
        addTip(successTopTip(g_var.gui.cover_stack[3].CoverFrame,f'欢迎登录 {g_var.User.basicInfo["username"]}'))

class LoginInput(ctk.CTkFrame):
    def __init__(self,master:LoginMain):
        super().__init__(master)
        ctk.CTkLabel(self,text="用户名：",font=("微软雅黑",16.5)).grid(row=0,column=0)
        ctk.CTkLabel(self,text="密   码：",font=("微软雅黑",16.5)).grid(row=1,column=0)
        self.usernameEntry:ctk.CTkEntry=ctk.CTkEntry(self,width=225,placeholder_text="你tm倒是填a")
        self.usernameEntry.grid(row=0,column=1,pady=11,padx=5.5)
        self.passwordEntey:ctk.CTkEntry=ctk.CTkEntry(self,width=225,placeholder_text="你tm倒是填a")
        self.passwordEntey.grid(row=1,column=1,pady=11,padx=5.5)
