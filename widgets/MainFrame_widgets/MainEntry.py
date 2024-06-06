from customtkinter import CTkTextbox

class MainEntry(CTkTextbox):
    def __init__(self, parent, width:int, height:int):
        super().__init__(parent)

        self.configure(width=width, height=height)