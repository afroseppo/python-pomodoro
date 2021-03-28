import tkinter as tk
import datetime as dt
import time

def timer(length: int, break_len: int) -> None:
    # Setting up the variables
    start_time = dt.datetime.now()
    pomodoro_length = dt.timedelta(minutes = length)
    end_time = start_time + pomodoro_length
    break_length = dt.timedelta(minutes = break_len)
    time_left = pomodoro_length

    countdown(time_left, end_time)

def countdown(time_left, end_time) -> None:
    while dt.datetime.now() < end_time:
        time_left = str(end_time - dt.datetime.now()).split('.')[0]
        print(time_left)
        time.sleep(1)
        
timer(5, 5)