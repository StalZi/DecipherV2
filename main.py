import customtkinter as ctk
from widgets import *

import json
with open("locales/widgets_en_us.json", "r") as read_file:
    locale = json.load(read_file)

VERSION: str = '2.0'
ctk.set_appearance_mode('dark')

class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title(f'Decipher V{VERSION}')
        self.geometry('900x500')
        self.minsize(500, 370)
        self.columnconfigure(index=0, weight=1)
        #self.rowconfigure(index=0, weight=1)
        #self.rowconfigure(index=1, weight=1)
        self.rowconfigure(index=2, weight=1)

        default_font: ctk.CTkFont = ctk.CTkFont('Verdana', 24, 'bold')

        self.main_frame: MainFrame = MainFrame(self, '#1a0500', 300, locale['content_frame_buttons'], default_font)
        self.upper_frame2: UpperFrame2 = UpperFrame2(self, '#424242', 45)
        self.upper_frame1: UpperFrame1 = UpperFrame1(self, self.upper_frame2, self.main_frame.content_frame, self.main_frame.main_entry_box, self.main_frame.main_entry_box2, locale, '#000000', 45, default_font)

        self.upper_frame1.grid(row=0, column=0, sticky='new')
        self.upper_frame2.grid(row=1, column=0, sticky='new')

        self.main_frame.grid(row=2, column=0, sticky='nsew')

        self.bind_all("<Key>", self._onKeyRelease, "+")

#        self.bind('<Configure>', lambda x: self.resize_text(upper_frame1, upper_frame2, main_frame))
#
#    def resize_text(self, upper_frame1, upper_frame2, main_frame):
#        size: int = (self.winfo_width() * self.winfo_height()) // 1000
#        font_size: int = int(size // 30)
#
#        all_children: list = upper_frame1.winfo_children() + upper_frame2.winfo_children() + main_frame.content_frame.winfo_children()
#
#        if font_size != all_children[0].cget('font').actual()['size']:
#            for child in all_children:
#                child.cget('font').configure(size=font_size)
#
#        if not upper_frame2.winfo_children():
#            upper_frame2_height = int(size // 10)
#            if upper_frame2_height != upper_frame2.cget('height'):
#                upper_frame2.configure(height=upper_frame2_height)

    def _onKeyRelease(self, event):
        ctrl = (event.state & 0x4) != 0
        if event.keycode==88 and ctrl and event.keysym.lower() != "x": 
            event.widget.event_generate("<<Cut>>")

        if event.keycode==86 and ctrl and event.keysym.lower() != "v": 
            event.widget.event_generate("<<Paste>>")

        if event.keycode==67 and ctrl and event.keysym.lower() != "c":
            event.widget.event_generate("<<Copy>>")

print(locale)
app = App()
app.mainloop()