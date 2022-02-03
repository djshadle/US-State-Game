import pandas

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()


class StateEngine:

    def __init__(self):
        self.data = pandas.read_csv("50_states.csv")
        self.states_list = data.state.to_list()
        self.correct_guesses = []
        self.need_practice = []

    def check_guess(self, guess: str):
        """Checks if guess is a correct state and if state has already been guessed"""
        if guess in self.states_list and guess not in self.correct_guesses:
            self.correct_guesses.append(guess)
            return True

    def states_to_learn(self):
        for state in self.states_list:
            if state not in self.correct_guesses:
                self.need_practice.append(state)
