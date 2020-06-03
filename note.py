from tkinter import *


class Note:
    def __init__(self, root, frame_row, frame_column):
        self.root = root
        self.frame = Frame(root)
        self.frame.grid(row=frame_row, column=frame_column)
        self.row_text = Entry(self.frame, width=32, borderwidth=10, justify='left', font=('calibri', 10))
        self.row_text.grid(row=0, column=0, columnspan=8, sticky='wens')
        self.row_text.insert(0, 'Enter any note you want here...')
