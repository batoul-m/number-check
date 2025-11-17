def check_number(target, guess):
    if guess > target:
        return "Number is bigger"
    elif guess < target:
        return "Number is smaller"
    else:
        return "Correct"


num = 15
print("choose number between 1 and 100")

num2 = 0
while num2 != num:
    num2 = int(input("Your guess: ")) 
    print(check_number(num, num2))