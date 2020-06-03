from winsound import *
from tkinter import *
import os


class PlayTheSound:
    def __init__(self, root, frame_row, frame_column):
        self.root = root
        self.frame = Frame(root)
        self.frame.grid(row=frame_row, column=frame_column)

        self.sound_choice = IntVar(None, 1)
        self.sound_on_off = IntVar()
        self.mute_checkbox = Checkbutton(self.frame, text='Mute:', variable=self.sound_on_off)

        self.sound_button_tone = Radiobutton(self.frame, text='Tone', variable=self.sound_choice, value=1)
        self.sound_button_rooster = Radiobutton(self.frame, text='Rooster', variable=self.sound_choice, value=2)
        self.sound_button_cuckoo_clock = Radiobutton(self.frame, text='CuckooClock', variable=self.sound_choice, value=3)

        self.sound_button_tone.grid(row=0, column=0, columnspan=3)
        self.sound_button_rooster.grid(row=0, column=3, columnspan=3)
        self.sound_button_cuckoo_clock.grid(row=0, column=6, columnspan=3)
        self.mute_checkbox.grid(row=0, column=9)

    @staticmethod
    def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    def play(self):
        sound_dict = {
            1: 'A-Tone-His_Self-1266414414.wav',
            2: 'Rooster Crow-SoundBible.com-1802551702.wav',
            3: 'Cuckoo Clock-SoundBible.com-1776874523.wav'
        }

        if self.sound_on_off.get() == 0:
            PlaySound(self.resource_path(str(sound_dict[self.sound_choice.get()])), SND_FILENAME)

        # if self.sound_on_off:
        #     PlaySound(str(sound_dict[self.sound_choice.get()]), SND_FILENAME)
        else:
            pass
