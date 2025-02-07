import tkinter as tk
from datetime import datetime
import calendar

from utils import ButtonTypes, DateButton, Date

class Calendar(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(self.parent)

        self.pack()

        self.create_widgets()

    def create_widgets(self):   
        self.control_frame = tk.Frame(self, width=400, height=50)
        self.control_frame.columnconfigure((0, 1, 2), weight=1)
        self.control_frame.pack(fill="x")

        self.pre_button = tk.Button(self.control_frame, text="<", command=self.pre_month, width=3, height=1, font=("Impact", 16), borderwidth=10)
        self.pre_button.grid(row=0, column=0)

        self.title_label = tk.Label(self.control_frame, text="", font=("Impact", 24), width=17)
        self.title_label.grid(row=0, column=1)

        self.nxt_button = tk.Button(self.control_frame, text=">", command=self.nxt_month, width=3, height=1, font=("Impact", 16), borderwidth=10)
        self.nxt_button.grid(row=0, column=2)

        self.calendar_frame = tk.Frame(self, width=400, height=400)
        self.calendar_frame.pack()

        self.update_calendar()

    def update_calendar(self):
        now_date = Date(datetime.now().day, datetime.now().month, datetime.now().year)

        for widget in self.calendar_frame.winfo_children():
            widget.destroy()
        self.title_label.config(text=f"{self.parent.month} / {self.parent.year}")

        days = ["SUN", "MON", "TUE", "WEN", "THU", "FRI", "SAT"]
        for col, day in enumerate(days):
            tk.Label(self.calendar_frame, text=day, font=("Impact", 16), padx=10).grid(row=0, column=col)

        cal = calendar.monthcalendar(self.parent.year, self.parent.month)
        
        i=0
        j=0
        for row, week in enumerate(cal, start=1):
            for col, day in enumerate(week):
                b_date = Date(day, self.parent.month, self.parent.year)
                if day == 0:
                    button = DateButton(self.calendar_frame , b_date.day, ButtonTypes.NONEDATE)
                else:
                    if(self.is_passed(now_date, b_date)):
                        button = DateButton(self.calendar_frame , b_date.day, ButtonTypes.PRE_DEFAULT)
                    else:
                        button = DateButton(self.calendar_frame , b_date.day, ButtonTypes.AFT_DEFAULT)
                    if(now_date.year == b_date.year and now_date.month == b_date.month and now_date.day == b_date.day):
                        button = DateButton(self.calendar_frame , b_date.day, ButtonTypes.NOW_DEFAULT)

                button.grid(row=row, column=col, padx=1)
                j+=1
            i+=1
        if i==5:
            for x in range(j-35, 7):
                button = DateButton(self.calendar_frame , b_date.day, ButtonTypes.NONEDATE)
                button.grid(row=6, column=x)

    def pre_month(self):
        if self.parent.month == 1:
            self.parent.month = 12
            self.parent.year -= 1
        else:
            self.parent.month -= 1
        self.update_calendar()

    def nxt_month(self):
        if self.parent.month == 12:
            self.parent.month = 1
            self.parent.year += 1
        else:
            self.parent.month += 1
        self.update_calendar()

    def is_passed(self, t_date:Date, b_date:Date):
        if(t_date.year > b_date.year):
            return True
        elif(t_date.year == b_date.year):
            if(t_date.month > b_date.month):
                return True
            elif(t_date.month == b_date.month and t_date.day > b_date.day):
                return True
        return False
