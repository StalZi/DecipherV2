from customtkinter import CTkButton, CTkFont

class DecipherButton(CTkButton):
    def __init__(self, parent, text:str, font:CTkFont, fg_color:str, hover_color:str):
        super().__init__(parent)

        self.configure(text=text, font=font, fg_color=fg_color, hover_color=hover_color, state='disabled')