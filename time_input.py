from tkinter import *


class TimeInput:
    def __init__(self, root, lbl_text, farme_row, frame_column):
        self.root = root
        self.frame = Frame(root)
        self.frame.grid(row=farme_row, column=frame_column)

        self.work_time_lbl = Label(self.frame, text='{}'.format(lbl_text), width=11, justify='center')
        self.work_time_h = Entry(self.frame, width=3, borderwidth=3, justify='center', font=10)
        self.dots = Label(self.frame, text=':', width=2, justify='center')
        self.work_time_m = Entry(self.frame, width=3, borderwidth=3, justify='center', font=10)
        self.dots1 = Label(self.frame, text=':', width=2, justify='center')
        self.work_time_s = Entry(self.frame, width=3, borderwidth=3, justify='center', font=10)

        self.work_time_lbl.grid(row=0, column=0, columnspan=3)

        self.work_time_h.grid(row=0, column=3)
        self.dots.grid(row=0, column=4)
        self.work_time_m.grid(row=0, column=5)
        self.dots1.grid(row=0, column=6)
        self.work_time_s.grid(row=0, column=7)

        self.work_time_h.insert(0, '00')
        self.work_time_m.insert(0, '00')
        self.work_time_s.insert(0, '00')

    def get_hours(self):
        return self.work_time_h.get()

    def get_seconds(self):
        return self.work_time_s.get()

    def get_minutes(self):
        return self.work_time_m.get()

    def get_time(self):
        return self.work_time_h.get(), self.work_time_m.get(), self.work_time_s.get()

    def clear(self):
        self.work_time_h.delete(0, END)
        self.work_time_m.delete(0, END)
        self.work_time_s.delete(0, END)

        self.work_time_h.insert(0, '00')
        self.work_time_m.insert(0, '00')
        self.work_time_s.insert(0, '00')

