from itertools import product
import random
import numpy as np


class Breaker():

    def __init__(self, maker_code=None, size_maker_passcode=5,
                 initial_colors=None):

        self.maker_code = maker_code
        self.size_maker_passcode = size_maker_passcode
        self.initial_colors = initial_colors
        self.colors_map = dict(zip(range(1, len(self.initial_colors) + 1), self.initial_colors))

    def initialize_move(self):
        combinations_of_breaker_code = list(product(range(1, self.size_maker_passcode + 1),
                                                    repeat=self.size_maker_passcode))
        self.move = random.sample(combinations_of_breaker_code, 1)
        self.move = [list(x) for x in self.move][0]
        return [self.colors_map[x] for x in self.move]

    def next_move(self, move):
        breaker_pass = [0] * self.size_maker_passcode
        for num in range(len(move)):
            if move[num] == self.maker_code[num]:
                breaker_pass[num] = self.maker_code[num]
            else:
                breaker_pass[num] = self.colors_map[random.randint(1, len(self.initial_colors))]

        return breaker_pass

    @staticmethod
    def Breaker_AI(lives, maker_code, size_maker_passcode, initial_colors):

        breaker = Breaker(maker_code=maker_code,
                          size_maker_passcode=size_maker_passcode,
                          initial_colors=initial_colors)

        initializemove = breaker.initialize_move()
        print(f"Life:{0}")
        print(f"Code:{initializemove}")
        life = 0

        while life < lives:

            initializemove = breaker.next_move(move=initializemove)
            print(f"Life:{life}")
            print(f"Code:{initializemove}")
            if initializemove == maker_code:
                print("YOY WIN!!")
            break
            life += 1


if __name__ == "__main__":
    breaker = Breaker
    breaker.Breaker_AI(lives=100,
                       maker_code=["BLACK", "BLUE", "GREEN", "ORANGE", "RED"],
                       size_maker_passcode=5,
                       initial_colors=["BLACK", "BLUE", "GREEN", "ORANGE", "RED", "YELLOW"])
