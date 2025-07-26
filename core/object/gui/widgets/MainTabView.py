import customtkinter as ctk

from core import g_var
from PIL import ImageTk,Image
from core import g_var

from core.object.gui.page.Login import LoginFrame
from core.object.gui.page.Home import homeFrame
from core.object.gui.page.TunnelManager import tunnelManagerFrame

class MainTabView(ctk.CTkTabview):

    mainTabMap={
        "登录":LoginFrame,
        "Home":homeFrame,
        "隧道管理":tunnelManagerFrame,
    }

    def __init__(self,master):
        super().__init__(master,height=480,width=810,corner_radius=13,fg_color="#ebebeb",segmented_button_fg_color="#bbc1c5",segmented_button_unselected_color="#bbc1c5",segmented_button_selected_color="#52b4a5",segmented_button_selected_hover_color="#42a495")
    
    # Override
    def _segmented_button_callback(self, selected_name):
        #self._tab_dict[self._current_name].grid_forget()
        self._current_name = selected_name
        self._set_grid_current_tab()
        self.upTabCoverWin()
        if self._command is not None:
            self._command()

    def add_tab(self,name:str):
        self.add(name)
        ctk.CTkLabel(self.tab(name),text="",image=ImageTk.PhotoImage(Image.open("./res/bg.jpg").resize((810,450)))).place(x=0,y=0)

    def upTabCoverWin(self):
        g_var.gui.cover_stack[0].setCoverFrame(self.mainTabMap[self.get()](g_var.gui.cover_stack[0]))