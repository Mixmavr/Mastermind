from itertools import product
import random
import numpy as np


class Breaker():

    def __init__(self, lives=8, maker_code=["BLACK", "BLUE", "GREEN", "ORANGE", "RED"], size_maker_passcode=5,
                 initial_colors=["BLACK", "BLUE", "GREEN", "ORANGE", "RED", "YELLOW"]):
        self.lives = lives
        self.maker_code = maker_code
        self.size_maker_passcode = size_maker_passcode
        self.initial_colors = initial_colors
        self.colors_map = dict(zip(self.initial_colors, range(1, len(self.initial_colors) + 1)))

        self.maker_code_pwd = []
        for i in range(len(self.maker_code)):
            self.maker_code_pwd.append(self.colors_map[self.maker_code[i]])

    def initialize_move(self):
        combinations_of_breaker_code = list(product(range(1, len(self.maker_code) + 1), repeat=5))
        self.move = random.sample(combinations_of_breaker_code, 1)
        self.move = [list(x) for x in self.move][0]
        return self.move

    def next_move(self, move):
        breaker_pass = [0] * self.size_maker_passcode
        for num in range(len(move)):
            if move[num] == self.maker_code_pwd[num]:
                breaker_pass[num] = self.maker_code_pwd[num]

        return breaker_pass


if __name__ == "__main__":

    lives = 8
    maker_code = ["BLACK", "BLUE", "GREEN", "ORANGE", "RED"]
    size_maker_passcode = 5
    initial_colors = ["BLACK", "BLUE", "GREEN", "ORANGE", "RED", "YELLOW"]
    breaker = Breaker(lives=lives, maker_code=maker_code,
                      size_maker_passcode=size_maker_passcode,
                      initial_colors=initial_colors)

    initializemove = breaker.initialize_move()

    life = 0

    while life < lives:
        print(f"Life:{life}")
        print(f"Code:{initializemove}")
        next_move = breaker.next_move(move=initializemove)
        if np.all((np.array(next_move) == 0)):
            initializemove = breaker.initialize_move()
        else:
            for i, elem in enumerate(next_move):
                if elem == 0:
                    next_move[i] = random.randint(1, len(initial_colors))
            initializemove = next_move

        life += 1

