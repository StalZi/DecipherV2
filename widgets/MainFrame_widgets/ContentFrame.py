from customtkinter import CTkFrame, CTkFont, CTkOptionMenu, StringVar
from widgets.MainFrame_widgets.ContentFrame_widgets import *
from ciphers import *

class ContentFrame(CTkFrame):
    def __init__(self, parent, locale:dict, font:CTkFont):
        super().__init__(parent)

        self.picked: int = -1
        self.language_optionmenu_var: StringVar = StringVar(value=locale['initial_values']['language_initial_value'])
        self.rot_optionmenu_var: StringVar = StringVar(value=locale['initial_values']['rot_initial_value'])

        self.decipher_button: DecipherButton = DecipherButton(self, locale['decipher_button'], font, '#253322', '#26a80c')
        self.decipher_button.grid(row=0, column=0, sticky='nsew', padx=10, pady=20)

    def frame_destroy(self):
        for child in self.winfo_children()[1:]:
            child.destroy()

    def caesar_pick(self, locale:dict, input_entry, output_entry):
        if self.picked == 0:
            return
        self.frame_destroy()

        self.language_options: CTkOptionMenu = CTkOptionMenu(self, values=[value for value in locale['language_dropdown'].values()], variable=self.language_optionmenu_var)
        self.rot_options: CTkOptionMenu = CTkOptionMenu(self, values=[value for value in locale['rot_dropdown'].values()], variable=self.rot_optionmenu_var)

        self.language_options.grid(row=1, column=0, padx=10, pady=20)
        self.rot_options.grid(row=2, column=0, padx=10, pady=20)

        self.decipher_button.configure(command=lambda: output_entry.output(caesar_dec(locale, self.language_optionmenu_var.get(), input_entry.get('0.0', 'end'), self.rot_optionmenu_var.get()), True))

        self.picked = 0

    def vigenere_pick(self, locale:dict, entry):
        if self.picked == 1:
            return
        self.frame_destroy()


        self.picked = 1
