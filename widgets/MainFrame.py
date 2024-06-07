from customtkinter import CTkFrame, CTkFont
from tkinter import PanedWindow
from widgets.MainFrame_widgets import *

class MainFrame(CTkFrame):
    def __init__(self, parent, color:str, height:int, locale:dict, font:CTkFont, decipher_button_fg_color:str, decipher_button_hover_color:str):
        super().__init__(parent)

        self.configure(fg_color=color, height=height)

        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=1)


        self.panel_divider = PanedWindow(master=self, orient='vertical', sashwidth=5, background=color)
        self.panel_divider_frame = CTkFrame(self.panel_divider, fg_color=color)

        self.content_panel_divider = PanedWindow(master=self.panel_divider, orient='horizontal', sashwidth=5, background='#000000')

        self.panel_divider.add(self.content_panel_divider)
        self.panel_divider.add(self.panel_divider_frame)

        self.main_entry_box: MainEntry = MainEntry(self.content_panel_divider, width=300, height=300)
        self.main_entry_box2: MainEntry2 = MainEntry2(self.content_panel_divider, width=300, height=300)
        self.content_frame: ContentFrame = ContentFrame(self.content_panel_divider, locale, font, decipher_button_fg_color, decipher_button_hover_color)

        self.content_panel_divider.add(self.main_entry_box)
        self.content_panel_divider.add(self.main_entry_box2)
        self.content_panel_divider.add(self.content_frame)

        self.panel_divider.grid(row=0, column=0, sticky='nsew')