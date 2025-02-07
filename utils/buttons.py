import tkinter as tk
from enum import Enum

class ButtonTypes(Enum):
    PRE_DEFAULT = "pre_default"
    NOW_DEFAULT = "now_default"
    AFT_DEFAULT = "aft_default"
    NOTDONE_DEFAULT = "notdone_default"
    DONE_DEFAULT = "done_default"
    NONEDATE = "nonedate"

class DateButton(tk.Button):
    def __init__(self, master, number, button_type : ButtonTypes):
        super().__init__(master)

        self.img = tk.PhotoImage(file=f"./assets/buttons/{button_type.value}.png")
        self.image_ref = self.img

        if button_type == ButtonTypes.NONEDATE:
            self.config(
                image=self.img,
                text="", font=("Impact", 18),
                compound="center",
                borderwidth=0,
                state="disabled",
            )
            return

        self.config(
            image=self.img,
            text=number, font=("Impact", 18),
            compound="center",
            borderwidth=0,
        )