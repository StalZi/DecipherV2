from customtkinter import CTkButton, CTkFont

class UpperFrameButton2(CTkButton):
    def __init__(self, parent, frame_to_change_widgets_in, input_entry, output_entry, locale:dict, row:int, column:int, text:str, font:CTkFont, id2:int):
        super().__init__(parent)

        self.configure(text=text, font=font)

        match id2:
            case 0:
                self.configure(command=lambda : frame_to_change_widgets_in.caesar_pick(locale['content_frame_buttons'], input_entry, output_entry))
            case 1:
                self.configure(command=lambda : frame_to_change_widgets_in.vigenere_pick(locale['content_frame_buttons'], input_entry, output_entry))

        self.grid(row=row, column=column, padx=10, pady=5)