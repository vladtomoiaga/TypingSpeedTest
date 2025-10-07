from tkinter import *
from gui import GUI
from controller import Controller
from scoreboard import Scoreboard
from timer import TimerApp

# Window
window = Tk()
window.title("Typing Speed Test App")
window.minsize(width=800, height=800)
window.config(padx=50, pady=50)

def start_typing_speed_test():
    scoreboard = Scoreboard()
    gui = GUI(window=window, scoreboard=scoreboard, controller=None, timer_app=None)
    timer_app = TimerApp(gui)
    controller = Controller(gui, scoreboard, timer_app)

    gui.set_buttons_control(controller, timer_app)

start_typing_speed_test()


window.mainloop()
