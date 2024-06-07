from customtkinter import CTkFrame, CTkFont
from widgets.UpperFrame1_widgets.UpperFrameButton1 import UpperFrameButton1

class UpperFrame1(CTkFrame):
    def __init__(self, parent, frame_to_change_buttons, frame_to_change_widgets_in, input_entry, output_entry,  locale:dict, bg:str, height:int, font:CTkFont):
        super().__init__(parent)

        self.configure(fg_color=bg, height=height)

        column: int = 1
        id: int = 0
        for button_name in locale['first_frame_buttons'].values():
            UpperFrameButton1(self, parent, 1, column, button_name, font, frame_to_change_buttons, frame_to_change_widgets_in, input_entry, output_entry, locale, id)
            #self.columnconfigure(index=column-1, weight=5)
            #self.columnconfigure(index=column, weight=1)
            #self.columnconfigure(index=column+1, weight=5)
            column += 3
            id += 1