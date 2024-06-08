from customtkinter import CTkFrame, CTkFont, CTkOptionMenu, CTkEntry, StringVar
from widgets.MainFrame_widgets.ContentFrame_widgets import *
from ciphers import *

class ContentFrame(CTkFrame):
    def __init__(self, parent, locale:dict, font:CTkFont, decipher_button_fg_color:str, decipher_button_hover_color:str):
        super().__init__(parent)
        self.locale: dict = locale
        self.picked: int = -1

        self.decipher_button: DecipherButton = DecipherButton(self, locale['decipher_button'], font, decipher_button_fg_color, decipher_button_hover_color)
        self.decipher_button.grid(row=0, column=0, sticky='nsew', padx=10, pady=20)

        self.language_optionmenu_var: StringVar = StringVar(value=locale['initial_values']['language_initial_value'])
        self.rot_optionmenu_var: StringVar = StringVar(value=locale['initial_values']['rot_initial_value'])
        self.language_options: CTkOptionMenu = CTkOptionMenu(self, variable=self.language_optionmenu_var)
        self.rot_options: CTkOptionMenu = CTkOptionMenu(self, variable=self.rot_optionmenu_var, state='disabled')
        self.key_entry: CTkEntry = CTkEntry(self, placeholder_text=locale['key_entry_placeholder'])

    def frame_destroy(self):
        for child in self.winfo_children()[1:]:
            child.grid_forget()
    
    def decipher_button_state_handler(self, locale:dict, has_language:bool = False, has_rot:bool = False):
        what_to_check: list[bool] = []

        if has_language:
            what_to_check.append(self.language_optionmenu_var.get() != locale['language_initial_value'])

        if has_rot:
            what_to_check.append(self.rot_optionmenu_var.get() != locale['rot_initial_value'])

        if all(what_to_check):
            self.decipher_button.configure(state='normal')
        else:
            self.decipher_button.configure(state='disabled')

    def language_dropdown_callback(self, locale:dict[str, dict[str, str]]):
        language_dropdown_values = self.locale['language_dropdown']
        language = self.language_optionmenu_var.get()

        if language == language_dropdown_values.get('all_languages'):
            values: list[str] = [str(rot) for rot in range(1, int(locale['rot_dropdown']['rot_all_languages']) + 1)]
            self.rot_options.configure(state='normal', values=[locale['rot_dropdown']['rot_all']] + values)

        elif language == language_dropdown_values.get('english'):
            values: list[str] = [str(rot) for rot in range(1, int(locale['rot_dropdown']['rot_english']) + 1)]
            if not self.rot_optionmenu_var.get() in values:
                self.rot_optionmenu_var.set(value=locale['initial_values']['rot_initial_value'])
            self.rot_options.configure(state='normal', values=[locale['rot_dropdown']['rot_all']] + values)

        elif language == language_dropdown_values.get('russian'):
            values: list[str] = [str(rot) for rot in range(1, int(locale['rot_dropdown']['rot_russian']) + 1)]
            if not self.rot_optionmenu_var.get() in values:
                self.rot_optionmenu_var.set(value=locale['initial_values']['rot_initial_value'])
            self.rot_options.configure(state='normal', values=[locale['rot_dropdown']['rot_all']] + values)


    def caesar_pick(self, locale:dict, window_to_bind_button_to, input_entry, output_entry):
        if self.picked == 0:
            return

        self.language_options.configure(values=[value for value in locale['language_dropdown'].values()], command=lambda x: [self.language_dropdown_callback(locale), self.decipher_button_state_handler(locale['initial_values'], True, True)])
        self.rot_options.configure(command=lambda x: self.decipher_button_state_handler(locale['initial_values'], True, True))

        self.frame_destroy()
        self.language_dropdown_callback(locale)

        self.language_options.grid(row=1, column=0, padx=10, pady=20)
        self.rot_options.grid(row=2, column=0, padx=10, pady=20)

        self.button_callback_function = lambda: output_entry.output(self.decipher_button, caesar_dec(locale, self.language_optionmenu_var.get(), input_entry.get('0.0', 'end'), self.rot_optionmenu_var.get()), True)
        self.decipher_button.configure(command=self.button_callback_function)
        window_to_bind_button_to.bind('<Return>', self.button_callback_function)

        self.picked = 0

    def vigenere_pick(self, locale:dict, window_to_bind_button_to, input_entry, output_entry):
        if self.picked == 1:
            return

        self.language_options.configure(values=[value for value in locale['language_dropdown'].values()][1:], command=lambda x: [self.language_dropdown_callback(locale), self.decipher_button_state_handler(locale['initial_values'], True)])

        self.frame_destroy()
        self.language_dropdown_callback(locale)
        if self.language_optionmenu_var.get() == locale['language_dropdown']['all_languages']:
            self.language_optionmenu_var.set(locale['initial_values']['language_initial_value'])
        
        self.language_options.grid(row=1, column=0, padx=10, pady=20)
        self.key_entry.grid(row=2, column=0, padx=10, pady=20)

        self.button_callback_function = lambda: output_entry.output(self.decipher_button, vigenere_dec(locale, self.language_optionmenu_var.get(), input_entry.get('0.0', 'end'), self.key_entry.get()))
        self.decipher_button.configure(command=self.button_callback_function)
        window_to_bind_button_to.bind('<Return>', self.button_callback_function)


        self.picked = 1

    def atbash_pick(self, locale:dict, window_to_bind_button_to, input_entry, output_entry):
        if self.picked == 1:
            return

        self.language_options.configure(values=[value for value in locale['language_dropdown'].values()], command=lambda x: [self.language_dropdown_callback(locale), self.decipher_button_state_handler(locale['initial_values'], True)])

        self.frame_destroy()
        self.language_dropdown_callback(locale)
        
        self.language_options.grid(row=1, column=0, padx=10, pady=20)

        self.button_callback_function = lambda: output_entry.output(self.decipher_button, atbash_dec(locale, self.language_optionmenu_var.get(), input_entry.get('0.0', 'end')))
        self.decipher_button.configure(command=self.button_callback_function)
        window_to_bind_button_to.bind('<Return>', self.button_callback_function)


        self.picked = 1