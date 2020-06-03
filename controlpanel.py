from tkinter import *


class ControlPanel:
    def __init__(self, root, frame_row, frame_column, start_timer, clear_timer, pause_timer, continue_clock, start_work_rest_timer):
        self.root = root
        self.frame = Frame(root)
        self.frame.grid(row=frame_row, column=frame_column, rowspan=8)

        self.start_button = Button(self.frame, text='Start!', command=start_timer)
        self.clear_button = Button(self.frame, text='Clear', command=clear_timer)
        self.pause_button = Button(self.frame, text='Pause', command=pause_timer)
        self.continue_button = Button(self.frame, text='Continue', command=continue_clock)
        self.start_work_rest = Button(self.frame, text='start work/rest timer', command=start_work_rest_timer)

        self.work_or_rest_lbl = Label(self.frame, fg='white', bg="orchid4", text='Work', width=12, justify='center')

        self.start_button.grid(row=0, column=0, sticky='wens', columnspan=2, rowspan=2)
        self.clear_button.grid(row=2, column=0, sticky='wens', columnspan=2, rowspan=2)
        self.pause_button.grid(row=4, column=0, sticky='wens', columnspan=2, rowspan=2)
        self.continue_button.grid(row=6, column=0, sticky='wens', columnspan=2, rowspan=2)
        self.start_work_rest.grid(row=8, column=0, sticky='wens', columnspan=2, rowspan=2)
        self.work_or_rest_lbl.grid(row=10, column=0, sticky='wens', columnspan=2, rowspan=4)
