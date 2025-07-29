import customtkinter as ctk
import tkinter
import core.g_var

from PIL import Image

from core.object.gui.widgets.CTkFrameG import CTkFrameG

class successTopTip(CTkFrameG):
    def __init__(self,master,text):
        super().__init__(master=master,AA=False)
        ctk.CTkLabel(self,text="",image=ctk.CTkImage(light_image=Image.open("./res/success.png"))).grid(row=0,column=0,pady=2,padx=(6,2),sticky="w")
        ctk.CTkLabel(self,text=text).grid(row=0,column=1,padx=(0,9),sticky="w")

    def pack(self,**kwargs):
        core.g_var.gui.main_win.after(2500,self.destroy)
        super().pack(**kwargs)

class errorTopTip(CTkFrameG):
    def __init__(self,master,text):
        super().__init__(master=master,AA=False)
        ctk.CTkLabel(self,text="",image=ctk.CTkImage(light_image=Image.open("./res/error.png"))).grid(row=0,column=0,pady=2,padx=(6,2),sticky="w")
        ctk.CTkLabel(self,text=text).grid(row=0,column=1,padx=(0,9),sticky="w")

    def pack(self,**kwargs):
        core.g_var.gui.main_win.after(2500,self.destroy)
        super().pack(**kwargs)

class MouseFollowTip(CTkFrameG):
    def __init__(self,master,smaster:ctk.CTkFrame,text,fg_color="gray90"):
        super().__init__(master=master,AA=False,fg_color=fg_color)
        self.tip:ctk.CTkLabel=ctk.CTkLabel(self,text=text)
        self.tip.grid(row=0,column=0,pady=0,padx=3)
        self.text=text
        self.master=master
        self.smaster=smaster
        self.smaster.bind("<Leave>",command=self.destroyTip,add="+")
        self.smaster.bind("<Motion>",command=self.moveTip,add="+")

    def destroyTip(self,event):
        self.tip.configure(text=self.text)
        self.place_forget()

    def moveTip(self,event):
        self.place(x=self.master.winfo_pointerx()-self.master.winfo_rootx(),y=self.master.winfo_pointery()-self.master.winfo_rooty()-self.winfo_height())
    
    def newText(self,newText):
        self.tip.configure(text=newText)