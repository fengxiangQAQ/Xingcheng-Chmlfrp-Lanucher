import customtkinter as ctk

import core.g_var as g_var

class PopWin(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master,corner_radius=0,width=785,height=418,fg_color="#0000ff")
    
    def place(self, **kwargs):
        g_var.gui.mask.update_mask()
        return super().place(**self._apply_argument_scaling(kwargs))
    
    def destroy(self):
        g_var.gui.mask.update_mask()
        super().destroy()