from customtkinter import CTkTextbox

class MainEntry2(CTkTextbox):
    def __init__(self, parent, width:int, height:int):
        super().__init__(parent)

        self.configure(width=width, height=height, state='disabled')

    def output(self, output:str|list, rot:bool = False):
        self.configure(state='normal')
        self.delete('0.0', 'end')


        if type(output) is str:
            final_output: str = output.rstrip() # type: ignore
        elif type(output) is list:
            if rot:
                final_output: list[str] = [] # type: ignore
                rot_number: int = 1
                for i in output:
                    final_output.append(f'ROT {rot_number} - {i}') # type: ignore
                    rot_number += 1
                final_output: str = ''.join(final_output).rstrip() # type: ignore
            else:
                final_output: str = ''.join(output).rstrip() # type: ignore

        self.insert('0.0', final_output) # type: ignore
        self.configure(state='disabled')