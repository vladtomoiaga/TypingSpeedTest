from tkinter import filedialog, END

class Controller:
    def __init__(self, gui, scoreboard, timer_app):
        self.gui = gui
        self.scoreboard = scoreboard
        self.timer_app = timer_app

        self.row = 0


    def open_file(self):
        """This method open a txt file"""
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

        if file_path:
            with open(file_path, 'r') as file:
                self.gui.text.set(file.read())
                self.gui.text_displayed = self.gui.text.get().splitlines()
                self.gui.text_to_be_copied.set(self.gui.text_displayed[self.row])

                self.gui.start_timer_button.config(state="normal")


    def verify_words(self, event):
        """This method verify if the words are written correct and in the right order"""
        words_typed = self.gui.text_typed.get().split()
        if len(self.gui.text_displayed) > 0:
            words_to_be_checked = self.gui.text_displayed[self.row].split()

            for word_to_be_checked, word_typed in zip(words_to_be_checked, words_typed):
                    # Check if the words are in the same order and are the same
                    if word_to_be_checked == word_typed:
                        self.scoreboard.increase_score()
                        self.gui.update_score_label()

            self.gui.text_input.delete(0,END)

            # Check if the number of the displayed row(from the text) is the same with the highest row number opened text
            if self.row == len(self.gui.text_displayed) - 1:
                self.timer_app.timer_running = False
                self.gui.text_input.config(state="disabled")
                self.gui.stop_timer_button.config(state="disabled")
                self.scoreboard.check_high_score()

            # Check if there are rows in the text
            elif self.row < len(self.gui.text_displayed) - 1:
                self.row += 1
                self.gui.text_to_be_copied.set(self.gui.text_displayed[self.row])
