from customtkinter import CTkFrame, CTkFont, CTkOptionMenu, StringVar
from widgets.MainFrame_widgets.ContentFrame_widgets import *
from ciphers import *

class ContentFrame(CTkFrame):
    def __init__(self, parent, locale:dict, font:CTkFont):
        super().__init__(parent)
        self.locale: dict = locale
        self.picked: int = -1
        self.language_optionmenu_var: StringVar = StringVar(value=locale['initial_values']['language_initial_value'])
        self.rot_optionmenu_var: StringVar = StringVar(value=locale['initial_values']['rot_initial_value'])

        self.decipher_button: DecipherButton = DecipherButton(self, locale['decipher_button'], font, '#253322', '#26a80c')
        self.decipher_button.grid(row=0, column=0, sticky='nsew', padx=10, pady=20)

    def frame_destroy(self):
        for child in self.winfo_children()[1:]:
            child.destroy()
    
    def decipher_button_state_handler(self, locale:dict):
        if self.language_optionmenu_var.get() != locale['language_initial_value'] and self.rot_optionmenu_var.get() != locale['rot_initial_value']:
            self.decipher_button.configure(state='normal')
        else:
            self.decipher_button.configure(state='disabled')

    def language_dropdown_callback(self, locale:dict[str, dict[str, str]]):
        language_dropdown_values = self.locale['language_dropdown']
        language = self.language_optionmenu_var.get()

        if language == language_dropdown_values.get('all_languages'):
            values: list = [str(rot) for rot in range(1, int(locale['rot_dropdown']['rot_all_languages']) + 1)]
            self.rot_options.configure(state='normal', values=values)
        elif language == language_dropdown_values.get('english'):
            values: list = [str(rot) for rot in range(1, int(locale['rot_dropdown']['rot_english']) + 1)]
            if not self.rot_optionmenu_var.get() in values:
                self.rot_optionmenu_var.set(value=locale['initial_values']['rot_initial_value'])
            self.rot_options.configure(state='normal', values=values)
        elif language == language_dropdown_values.get('russian'):
            values: list = [str(rot) for rot in range(1, int(locale['rot_dropdown']['rot_russian']) + 1)]
            if not self.rot_optionmenu_var.get() in values:
                self.rot_optionmenu_var.set(value=locale['initial_values']['rot_initial_value'])
            self.rot_options.configure(state='normal', values=values)

        self.decipher_button_state_handler(locale['initial_values'])


    def caesar_pick(self, locale:dict, input_entry, output_entry):
        if self.picked == 0:
            return
        self.frame_destroy()
        self.language_dropdown_callback(locale)

        self.language_options: CTkOptionMenu = CTkOptionMenu(self, values=[value for value in locale['language_dropdown'].values()], variable=self.language_optionmenu_var, command=lambda x: self.language_dropdown_callback(locale))
        self.rot_options: CTkOptionMenu = CTkOptionMenu(self, variable=self.rot_optionmenu_var, state='disabled', command=lambda x: self.decipher_button_state_handler(locale['initial_values']))

        self.language_options.grid(row=1, column=0, padx=10, pady=20)
        self.rot_options.grid(row=2, column=0, padx=10, pady=20)

        self.decipher_button.configure(command=lambda: output_entry.output(caesar_dec(locale, self.language_optionmenu_var.get(), input_entry.get('0.0', 'end'), self.rot_optionmenu_var.get()), True))

        self.picked = 0

    def vigenere_pick(self, locale:dict, input_entry, output_entry):
        if self.picked == 1:
            return
        self.frame_destroy()
        self.decipher_button_state_handler(locale['initial_values'])

        self.decipher_button.configure(command=None) # for now


        self.picked = 1
