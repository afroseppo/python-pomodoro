import tkinter as tk
import datetime as dt

class App():
    def __init__(self, length: int):
        self.root = tk.Tk()
        self.root.geometry('480x360')
        self.message = tk.Label(text = 'Currently on a Pomodoro')
        self.label = tk.Label(text = '')
        self.pomodoros = tk.Label(text = 'Pomodoros: ')
        self.pomodoro_count = 0

        self.reset_button = tk.Button(text = 'Reset', command = self.reset_clock)
        self.start_button = tk.Button(text = 'Start', command = self.start_countdown)
        self.pause_button = tk.Button(text = 'Pause', command = self.pause_countdown)

        self.length = dt.timedelta(minutes = length)
        self.time_left = self.length
        self.set_time(self.time_left)

        self.message.pack()
        self.label.pack()
        self.reset_button.pack()
        self.start_button.pack()
        self.pause_button.pack()
        self.pomodoros.pack()

        self.is_break = False
        self.is_running = True

        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        if self.time_left == dt.timedelta(seconds = 0) and not self.is_break:
            self.is_break = True
            self.time_left = dt.timedelta(minutes = 5)
            self.message.config(text = 'Currently on a break')
            self.pomodoro_count += 1
        elif self.is_break and self.time_left == dt.timedelta(seconds = 0) :
            self.is_break = False
            self.time_left = dt.timedelta(minutes = self.length)
            self.message.config(text = 'Currently on a Pomodoro')

        if self.is_running:
            self.time_left -= dt.timedelta(seconds = 1)
            self.set_time(self.time_left)

        self.root.after(1000, self.update_clock)

    def start_countdown(self):
        self.is_running = True

    def pause_countdown(self):
        self.is_running = False

    def reset_clock(self):
        self.time_left = self.length
        self.set_time(self.time_left)
        self.running = False

    def set_time(self, time_to_set):
        time_left_string = str(time_to_set).split('.')[0]
        self.label.config(text = time_left_string)


pomodoro = App(10)