import customtkinter as ctk

class MaskFrame(ctk.CTkFrame):
    
    mask=False

    def __init__(self,master):
        super().__init__(master,width=784,height=418,corner_radius=0,fg_color="#0000ff")
    
    def update_mask(self):
        self.mask=not self.mask
        if self.mask:
            self.configure(fg_color="#000000")
        else:
            self.configure(fg_color="#0000ff")