import tkinter as tk

from gui.widgets import Options, Calendar
from datetime import datetime

from configs import UI_WINDOW_NAME, UI_WINDOW_SIZE

class Primary(tk.Frame):
    def __init__(self, root : tk.Tk):
        self.root = root
        super().__init__(self.root)

        # self.root.resizable(False, False)
        self.master.title(UI_WINDOW_NAME)
        self.master.geometry(f"{UI_WINDOW_SIZE[0]}x{UI_WINDOW_SIZE[1]}")

        self.pack(fill="both")

        self.top_frame = Options(self)
        self.main_frame = tk.Frame(self)

        self.top_frame.pack(fill="x")
        self.main_frame.pack(fill="x")

        self.month = datetime.now().month
        self.year = datetime.now().year
        
        self.to_calendar()
    
    def to_settings(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def to_calendar(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        calendar = Calendar(self)
        calendar.pack()

    def to_appearance(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
