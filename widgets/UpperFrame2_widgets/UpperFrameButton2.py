from customtkinter import CTkButton, CTkFont

class UpperFrameButton2(CTkButton):
    def __init__(self, parent, window_to_bind_button_to, frame_to_change_widgets_in, input_entry, output_entry, locale:dict, row:int, column:int, text:str, font:CTkFont, id2:int):
        super().__init__(parent)

        self.configure(text=text, font=font)
        arguments = (locale['content_frame_buttons'], window_to_bind_button_to, input_entry, output_entry)

        match id2:
            case 0:
                self.configure(command=lambda : frame_to_change_widgets_in.caesar_pick(*arguments))
            case 1:
                self.configure(command=lambda : frame_to_change_widgets_in.vigenere_pick(*arguments))
            case 2:
                self.configure(command=lambda : frame_to_change_widgets_in.atbash_pick(*arguments))
            case 3:
                self.configure(command=lambda : frame_to_change_widgets_in.playfair_pick(*arguments))
            case 4:
                self.configure(command=lambda : frame_to_change_widgets_in.a1z26_pick(*arguments))

        self.grid(row=row, column=column, padx=10, pady=5)