from tkinter import *


class TimeShow:
    def __init__(self, root, farme_row, frame_column):
        self.root = root
        self.frame = Frame(root)
        self.frame.grid(row=farme_row,column=frame_column)

        self.lbl_time = Label(self.root, font=('calibri', 30, 'bold'), background='purple', foreground='white')
        self.lbl_time.grid(row=2, rowspan=3, column=0, columnspan=5, sticky='wens')

    def config_display(self,  time_to_config='0:0:0'):
        self.lbl_time.config(text=time_to_config)
