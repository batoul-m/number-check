import random

class Number:
    def __init__(self):
        self.target = random.randint(1, 100)

    def __eq__(self, other):
        return self.target == other

    def check(self, guess):
        if guess > self.target:
            return "Number is bigger"
        elif guess < self.target:
            return "Number is smaller"


game = Number()

print("Guess a number between 1 and 100")

guess = None

while guess != game.target:
    guess = int(input("Your guess: "))

    if game == guess:
        print("Correct!")
        break
    else:
        print(game.check(guess))
