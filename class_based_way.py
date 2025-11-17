class CheckNumber:
    def __init__(self, target):
        self.target = target
        self._guess = None

    @property
    def guess(self):
        return self._guess

    @guess.setter
    def guess_setter(self, guess):
        self._guess = guess

    def check_number(self):
        if self._guess > self.target:
            return "Number is bigger"
        elif self._guess < self.target:
            return "Number is smaller"
        else:
            return "Correct"
        

num = 15
print("choose number between 1 and 100")
guess_check = CheckNumber(num)

num2 = 0
while num2 != num:
    num2 = int(input("Your guess: "))
    guess_check.guess_setter = num2 
    print(guess_check.check_number())