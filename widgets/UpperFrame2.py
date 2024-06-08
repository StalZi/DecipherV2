from customtkinter import CTkFrame, CTkFont
from widgets.UpperFrame2_widgets.UpperFrameButton2 import UpperFrameButton2

class UpperFrame2(CTkFrame):
    def __init__(self, parent, bg:str, height:int):
        super().__init__(parent)

        self.configure(fg_color=bg, height=height)

        #self.grid_rowconfigure(index=0, weight=1)
        #self.grid_rowconfigure(index=1, weight=2)
        #self.grid_rowconfigure(index=2, weight=1)

        self.picked: int = -1

    def frame_destroy(self):
        for child in self.winfo_children():
            #column: int = child.grid_info()['column']
            #self.columnconfigure(index=column-1, weight=0)
            #self.columnconfigure(index=column, weight=0)
            #self.columnconfigure(index=column+1, weight=0)
            child.destroy()


    def ciphers_pick(self, window_to_bind_button_to, frame_to_change_in, input_entry, output_entry, locale:dict, font:CTkFont):
        if self.picked == 0:
            return

        self.frame_destroy()
        
        column: int = 1
        id2: int = 0
        for button_name in locale['upper_frame_buttons1'].values():
            UpperFrameButton2(self, window_to_bind_button_to, frame_to_change_in, input_entry, output_entry, locale, 1, column, button_name, font, id2)
            #self.columnconfigure(index=column-1, weight=4)
            #self.columnconfigure(index=column, weight=1)
            #self.columnconfigure(index=column+1, weight=4)
            column += 3
            id2 += 1
        
        self.picked = 0

    def alphabets_pick(self, window_to_bind_button_to, frame_to_change_in, input_entry, output_entry, locale:dict, font:CTkFont):
        if self.picked == 1:
            return

        self.frame_destroy()

        column: int = 1
        id2: int = 0
        for button_name in locale['upper_frame_buttons2'].values():
            UpperFrameButton2(self, window_to_bind_button_to, frame_to_change_in, input_entry, output_entry, locale, 1, column, button_name, font, id2)
            #self.columnconfigure(index=column-1, weight=4)
            #self.columnconfigure(index=column, weight=1)
            #self.columnconfigure(index=column+1, weight=4)
            column += 3
            id2 += 1

        self.picked = 1