from config import TIME

class TimerApp:
    def __init__(self, gui):
        self.gui = gui

        # Initialize timer variables
        self.seconds = TIME
        self.timer_running = False


    def start_timer(self):
        """This method start the timer"""
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

            self.gui.start_game()


    def stop_timer(self):
        """This method stops the timer"""
        self.timer_running = False
        self.gui.stop_game()


    def update_timer(self):
        """This method update the timer. Ex:Timer is going from 60 sec to 0 seconds"""
        if self.timer_running:
            if self.seconds >= 1:
                self.seconds -= 1
                self.gui.update_time_label()
                self.gui.window.after(1000, self.update_timer)  # Update every 1 second
            else:
                self.stop_timer()
                self.gui.update_time_label()


    def reset_timer(self):
        """This method reset the timer"""
        self.timer_running = False
        self.seconds = TIME
        self.gui.update_time_label()

        self.gui.reset_game()
