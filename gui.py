from tkinter import Label, Entry, Button, StringVar, END

FONT = ("Arial", 14)
FONT_TIMER = ("Arial", 20)

class GUI:

    def __init__(self, window, scoreboard, controller, timer_app):
        self.window = window
        self.scoreboard = scoreboard
        self.controller = controller
        self.timer_app = timer_app

        self.text = StringVar(value="")
        self.text_displayed = []
        self.text_to_be_copied = StringVar(value="")

        self.text_typed = StringVar(value="")

        self.gui_setup()

    def gui_setup(self):
        """This method configs the GUI"""
        self.labels()
        self.entries()
        self.buttons()

    # Labels
    def labels(self):
        """This method create all the labels for the GUI"""
        Label(self.window, text="Current CPM", font=FONT).grid(column=0, row=1, padx=10, pady=10)
        Label(self.window, text="Highest CPM", font=FONT).grid(column=0, row=2, padx=10, pady=10)

        self.current_cpm_label = Label(self.window, textvariable=self.scoreboard.current_score, font=FONT)
        self.current_cpm_label.grid(column=1, row=1, padx=10, pady=10)

        self.highest_cpm_label = Label(self.window, textvariable=self.scoreboard.high_score, font=FONT)
        self.highest_cpm_label.grid(column=1, row=2, padx=10, pady=10)

        self.time_text_label = Label(self.window, text="Time", font=FONT)
        self.time_text_label.grid(column=0, row=3, padx=10, pady=10)

        time_remaining = f"{self.timer_app.seconds:02}" if self.timer_app else "00"
        self.time_label = Label(self.window, text=time_remaining, font=FONT)
        self.time_label.grid(column=1, row=3, padx=10, pady=10)

        Label(self.window, textvariable=self.text, font=FONT).grid(column=0, row=4, rowspan=2, padx=10, pady=10)

        self.text_to_be_copied_label = Label(self.window, textvariable=self.text_to_be_copied, font=FONT)
        self.text_to_be_copied_label.grid(column=1, row=4, rowspan=2, padx=10, pady=10)


    def update_time_label(self):
        """This method update the time label"""
        if self.timer_app:
            time_str = f"{self.timer_app.seconds:02}"
            self.time_label.config(text=time_str)


    def update_score_label(self):
        """This method update the score label"""
        self.current_cpm_label.config(textvariable=self.scoreboard.current_score)

    # Entries
    def entries(self):
        """This method create the entries necessary for the GUI"""
        self.text_input = Entry(self.window, textvariable=self.text_typed, width=50)
        self.text_input.grid(column=1, row=6, padx=10, pady=10)
        self.text_input.config(state="disabled")

    # Buttons
    def buttons(self):
        """This method create all the buttons for the GUI"""
        self.open_button = Button(self.window, text="Open File", command=None)
        self.open_button.grid(column=0, row=0, padx=10, pady=10)

        self.start_timer_button = Button(self.window, text="Start", command=None)
        self.start_timer_button.grid(column=1, row=0, padx=10, pady=10)
        self.start_timer_button.config(state="disabled")

        self.stop_timer_button = Button(self.window, text="Stop", command=None)
        self.stop_timer_button.grid(column=2, row=0, padx=10, pady=10)
        self.stop_timer_button.config(state="disabled")

        self.reset_timer_button = Button(self.window, text="Reset", command=None)
        self.reset_timer_button.grid(column=3, row=0, padx=10, pady=10)
        self.reset_timer_button.config(state="disabled")

    # The following methods set the state of the buttons and labels in different situation of the game
    def set_buttons_control(self, controller, timer_app):
        """This method creates all the necessary for the game to start"""
        self.controller = controller
        self.timer_app = timer_app

        self.open_button.config(command=self.controller.open_file)
        self.text_input.bind('<Key-Return>', self.controller.verify_words)

        self.start_timer_button.config(command=self.timer_app.start_timer)
        self.stop_timer_button.config(command=self.timer_app.stop_timer)
        self.reset_timer_button.config(command=self.timer_app.reset_timer)


    def start_game(self):
        """This method config all the status for GUI when the game starts"""
        self.text_input.config(state="normal")
        self.text_input.delete(0, END)
        self.text_input.focus() # The user can start typing directly in this entry without making a click in the entry

        self.start_timer_button.config(state="disabled")
        self.stop_timer_button.config(state="normal")
        self.reset_timer_button.config(state="normal")


    def stop_game(self):
        """This method config all the status for GUI when the game stops"""
        self.start_timer_button.config(state="normal")
        self.stop_timer_button.config(state="disabled")
        self.text_input.config(state="disabled")
        self.scoreboard.check_high_score()


    def reset_game(self):
        """This method config all the status for GUI when the game resets"""
        self.stop_game()

        self.reset_timer_button.config(state="disabled")
        self.text_input.delete(0, END)
        self.controller.row = 0
        self.text_to_be_copied.set(self.text_displayed[self.controller.row])

        self.scoreboard.check_high_score()
        self.scoreboard.current_score.set(0)
        self.highest_cpm_label.config(textvariable=self.scoreboard.high_score)

    # End of the methods for the state of the buttons and labels
    ######################################################################
