from turtle import Turtle
import pandas

data = pandas.read_csv("50_states.csv")

FONT = ("Verdana", 15, "normal")


class WriteState(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_answer(self, answer):
        state_row = data[data.state == answer]
        state_x = int(state_row["x"])
        state_y = int(state_row["y"])
        self.goto(state_x, state_y)
        self.write(answer, align="center", font=FONT)
