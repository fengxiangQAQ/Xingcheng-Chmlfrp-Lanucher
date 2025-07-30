import customtkinter as ctk
import win32clipboard

from core.object.gui.widgets.PanelButton import PanelBButton,PanelRButton
from core.object.gui.widgets.tip import MouseFollowTip
from core.object.gui.widgets.CTkFrameG import CTkFrameG
from core.object.gui.widgets.CTkButtonG import CTkButtonG
from core.object.gui.widgets.tip import successTopTip,errorTopTip
from core.object.gui.popWIN.ConfirmPopWin import ConfirmPopWin
from core.utils.network.ChmlfrpApi import APIv1
from core.utils.runFrpc import runFrpc
from core.WinManager import addTip
import core.g_var

class tunnelManagerFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,width=783,height=418,corner_radius=0,fg_color="#0000ff")
        self.after(1000,core.g_var.User.updateTunnel)
        tunnelManagerMain(self).pack()

class tunnelManagerMain(ctk.CTkScrollableFrame):
    def __init__(self,master):
        super().__init__(master,width=769,height=418,corner_radius=0,fg_color="#0000ff",scrollbar_button_color="gray65",scrollbar_button_hover_color="gray60")
        self.add_tun_card=CTkButtonG(self,text="+",font=("微软雅黑",60),fg_color="#e9e9e9",hover_color="#e5e5e5",text_color="#c3c3c3",width=245,height=183,corner_radius=12,AA=False)
        self.add_tun_card.grid(row=0,column=0,pady=7,padx=6)
        self.after(100,self.build)

    def build(self):
        k=1
        for i in core.g_var.User.TunnelDict:
            tunnelCard(self,core.g_var.User.TunnelDict[i]).grid(row=int(k/3),column=int(k%3),pady=7,padx=6)
            k+=1

class tunnelCard(CTkFrameG):
    def __init__(self,master,info:dict):
        super().__init__(master,fg_color="#e5e5e5",width=245,height=183,corner_radius=12,AA=False)
        self.tun_id=info["id"]
        self.tun_name=info["name"]
        ctk.CTkLabel(self,text=f"#{self.tun_id}",font=("微软雅黑",15.5)).place(x=13,y=7)
        ctk.CTkLabel(self,text=info["name"],font=("微软雅黑",15.5,"bold")).place(x=(len(str(info["id"]))+2)*9+12,y=7)
        ctk.CTkLabel(self,text="内网地址: "+info["localip"]+":"+str(info["nport"])+" - "+info["type"],font=("微软雅黑",13)).place(x=13,y=37)
        ctk.CTkLabel(self,text="节点信息: "+info["node"],font=("微软雅黑",13)).place(x=13,y=57)
        try:
            if info["type"] in ["http",'https']:
                self.cUrl=info["dorp"]
            else:
                self.cUrl=info["ip"]+":"+info["dorp"]
        except:
            self.cUrl=""
        cUrlLabel=ctk.CTkLabel(self,text="连接地址: "+self.cUrl,font=("微软雅黑",13))
        cUrlLabel.bind("<ButtonPress-1>",self.copyUrl)
        cUrlLabel.place(x=13,y=77)
        self.tip:MouseFollowTip=MouseFollowTip(core.g_var.gui.cover_stack[3],cUrlLabel,"点击以复制",fg_color="gray92")
        PanelBButton(self,text="启动隧道",width=219,command=self.startFrp).place(x=13,y=108)
        PanelRButton(self,text="删除隧道",width=219,command=self.deltunnel).place(x=13,y=143)

    def deltunnel(self):
        core.g_var.gui.cover_stack[2].setCoverFrame(ConfirmPopWin(core.g_var.gui.cover_stack[2],text=f"您正在删除隧道#{self.tun_id} {self.tun_name}，请确认是否删除",callbackFun=self.confirm_deltunnel,confirm_color="#F0A020",confirm_hover_color="#FCB040",title="警告"))

    def confirm_deltunnel(self,b:bool):
        if b:
            state,tip=APIv1.delTunnel(core.g_var.User.token,core.g_var.User.id,self.tun_id)
            if state:
                addTip(successTopTip(core.g_var.gui.cover_stack[3].CoverFrame,tip))
            else:
                addTip(errorTopTip(core.g_var.gui.cover_stack[3].CoverFrame,tip))
            core.g_var.User.updateTunnel()
            core.g_var.gui.main_win.main_tab_view.upTabCoverWin()
        else:
            addTip(errorTopTip(core.g_var.gui.cover_stack[3].CoverFrame,"已取消操作"))

    def startFrp(self):
        runFrpc(frpcPath="./res/frpc.exe",runDir=".\XCL",userToken=core.g_var.User.token,tunnelID=self.tun_id)
        
    def copyUrl(self,event):
        self.tip.newText("已复制")
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT,self.cUrl)
        win32clipboard.CloseClipboard()