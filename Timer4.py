from tkinter import *
import time

from controlpanel import ControlPanel
from note import Note
from time_show import TimeShow
from time_input import TimeInput
from sound_wav import PlayTheSound


class Clock:
    def __init__(self, root):
        self.root = root
        self.root.title('Timer')
        self.root.iconbitmap('C:\\Users\\Adi Tal\\PycharmProjects\\Tkinter_Projects\\timer3\\clock_icon.ico')
        self.clock_running = False
        self.is_work_flag = True
        self.continuation = False
        self.total_time = 0
        self.work_time = 0
        self.rest_time = 0
        self.clock_h = 0
        self.clock_m = 0
        self.clock_s = 0


        # frames from different class
        self.free_note = Note(root, 0, 0)
        self.timer_reg = TimeInput(root, 'Main Timer', 1, 0)
        self.display_of_time = TimeShow(root, 2, 0)
        self.work_time_input = TimeInput(root, 'Work time', 7, 0)
        self.rest_time_input = TimeInput(root, 'Rest time', 8, 0)
        self.sound_frame = PlayTheSound(root, 9, 0)
        self.control_panel = ControlPanel(root, 0, 1, self.start_regular_timer, self.clear_func, self.pause_clock, self.continue_clock, self.start_work_rest_timer)

    # buttons functions
    def pause_clock(self):
        self.clock_running = False

    def continue_clock(self):
        self.clock_running = True
        self.countdown(self.clock_h, self.clock_m, self.clock_s)

    def clear_func(self):
        self.work_time_input.clear()
        self.rest_time_input.clear()
        self.timer_reg.clear()

        self.continuation = False
        self.display_of_time.config_display()

    # Time conversion help functions
    @staticmethod
    def convert_sec_to_time(time_left):
        hh = int(time_left / 3600)
        mm = int(((time_left / 3600) - hh) * 60)
        ss = round(((((time_left / 3600) - hh) * 60) - mm) * 60)
        return hh, mm, ss

    @staticmethod
    def con_time_to_sec(h, m, s):
        sec = (int(h) * 3600) + (int(m) * 60) + int(s)
        return sec

    # main clock countdown functions
    def start_regular_timer(self):
        self.clock_running = True
        self.continuation = False
        self.countdown(*self.timer_reg.get_time())

    def start_work_rest_timer(self):
        self.clock_running = True
        self.continuation = True
        self.work_rest_countdown()

    def work_rest_countdown(self):
        self.work_time = int(self.con_time_to_sec(*self.work_time_input.get_time()))
        self.rest_time = int(self.con_time_to_sec(*self.rest_time_input.get_time()))

        if self.is_work_flag:
            self.is_work_flag = False
            self.control_panel.work_or_rest_lbl.config(text='Work', bg='orchid4')
            h, m, s = self.convert_sec_to_time(self.work_time)
        else:
            self.is_work_flag = True
            self.control_panel.work_or_rest_lbl.config(text='Rest', bg='sky blue')
            h, m, s = self.convert_sec_to_time(self.rest_time)

        self.countdown(h, m, s)

    def countdown(self, h, m, s):
        sec = int(self.con_time_to_sec(h, m, s))
        if time.perf_counter() < time.perf_counter() + sec and self.clock_running:
            self.clock_h, self.clock_m, self.clock_s = self.convert_sec_to_time(sec)
            time_l = '{}:{}:{}'.format(self.clock_h, self.clock_m, self.clock_s)
            self.display_of_time.config_display(time_l)
            hh, mm, ss = self.convert_sec_to_time(sec - 1)
            self.display_of_time.lbl_time.after(1000, lambda: self.countdown(hh, mm, ss))

        elif self.clock_running and self.continuation:
            self.sound_frame.play()
            self.work_rest_countdown()

        elif self.clock_running and self.continuation is False:
            self.sound_frame.play()
        else:
            pass


root = Tk()
my_timer1 = Clock(root)

root.mainloop()
