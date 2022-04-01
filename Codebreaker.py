
class CodeBreaker():
    def __init__(self):
        pass

    def makeGuess(self):
        epitrepta_xrwmata = ['blue', 'green','orange','yellow','black','purple']

        guesses = input('Give color combination :').split('-')
        for colour in guesses:
            if colour in epitrepta_xrwmata:
                pass

            else:
                print("Η τιμή που δώσατε δεν είναι σωστή")
                continue


        return guesses





class Menu():
    def __init__(self):
        while True:
            print(CodeBreaker.makeGuess(self))
            


if __name__ == "__main__": Menu()

