import turtle
import pandas
from write_state import WriteState
from state_engine import StateEngine

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
write = WriteState()
state_engine = StateEngine()


def screen_pop():
    guessed_states = len(state_engine.correct_guesses)
    if guessed_states == 0:
        title = "Guess the State"
    else:
        title = f"{guessed_states}/50 States Correct"
    return screen.textinput(title=title, prompt="What's another state name?").title()


while len(state_engine.correct_guesses) != 50:
    users_guess = screen_pop()
    if users_guess == "Exit":
        break
    if state_engine.check_guess(users_guess):
        write.write_answer(users_guess)


# states_to_learn.csv
state_engine.states_to_learn()
df = pandas.DataFrame(state_engine.need_practice, columns=["Need Practice:"])
df.to_csv('states_to_learn.csv', index=False)



