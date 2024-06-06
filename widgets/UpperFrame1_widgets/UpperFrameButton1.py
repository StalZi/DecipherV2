from customtkinter import CTkButton, CTkFrame, CTkFont

class UpperFrameButton1(CTkButton):
    def __init__(self, parent, row:int, column:int, text:str, font:CTkFont, frame_to_change_buttons, frame_to_change_widgets_in, input_entry, output_entry, locale:dict, id:int):
        super().__init__(parent)

        self.configure(text=text, font=font)
        
        match id:
            case 0:
                self.configure(command=lambda : frame_to_change_buttons.ciphers_pick(frame_to_change_widgets_in, input_entry, output_entry, locale, font))
            case 1:
                self.configure(command=lambda : frame_to_change_buttons.alphabets_pick(frame_to_change_widgets_in, input_entry, output_entry, locale, font))

        self.grid(row=row, column=column, padx=10, pady=5)