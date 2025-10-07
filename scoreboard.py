from tkinter import IntVar

class Scoreboard:
    def __init__(self):
        self.current_score = IntVar(value=0)

        try:
            with open("highscore.txt") as data:
                highest_score = data.read()
                self.high_score = IntVar(value=int(highest_score) if highest_score else 0)
        except FileNotFoundError:
            with open("highscore.txt", "w") as data:
                data.write("0")
            self.high_score = IntVar(value=0)


    def increase_score(self):
        """This method increase the score"""
        self.current_score.set(self.current_score.get() + 1)
        return self.current_score


    def check_high_score(self):
        """This method checks if the highscore is reached or not"""
        if self.current_score.get() > self.high_score.get():
            self.high_score.set(self.current_score.get())
            with open("highscore.txt", mode="w") as data:
                data.write(f"{self.high_score.get()}")
