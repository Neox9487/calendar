import tkinter as tk

from configs import UI_WINDOW_SIZE

class Options(tk.Frame):
    def __init__(self, master : tk.Frame):
        super().__init__(master, width=UI_WINDOW_SIZE[0] - 20)

        self.columnconfigure((0, 1, 2), weight=1)

        self.master = master
        self.options = ["Settings", "Calendar", "Appearance"]

        self.create_widgets()

    def create_widgets(self):
        for i, text in enumerate(self.options):
            button = tk.Button(
                self,
                width=12,
                text=text,
                command = lambda t=text : self.on_clicked(t),
                font=("Impact", 13),
                borderwidth=10
            )
            button.grid(
                column=i, 
                row=0,
                padx=12, pady=3, 
                sticky="ew"
            )

    def on_clicked(self, text):
        if text == self.options[0]:
            self.master.to_settings()
        elif text == self.options[1]:
            self.master.to_calendar()
        elif text == self.options[2]:
            self.master.to_appearance()