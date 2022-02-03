import turtle
import pandas
from write_state import WriteState

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
screen.addshape(image)
correct_guesses = []
turtle.shape(image)
write = WriteState()


def check_guess(guess: str, states: list, answers: list):
    """Checks if guess is a correct state and if state has already been guessed"""
    if guess in states and guess not in answers:
        correct_guesses.append(users_guess)
        write.write_answer(users_guess)


def screen_pop():
    guessed_states = len(correct_guesses)
    if guessed_states == 0:
        title = "Guess the State"
    else:
        title = f"{guessed_states}/50 States Correct"
    return screen.textinput(title=title, prompt="What's another state name?").title()


def states_to_learn():
    need_practice = []
    for state in states_list:
        if state not in correct_guesses:
            need_practice.append(state)
        df = pandas.DataFrame(need_practice, columns=["Need Practice:"])
        df.to_csv('states_to_learn.csv', index=False)


while len(correct_guesses) != 50:
    users_guess = screen_pop()
    if users_guess == "Exit":
        break
    check_guess(users_guess, states_list, correct_guesses)

# states_to_learn.csv
states_to_learn()



