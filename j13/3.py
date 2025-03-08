from operator import ge
import random as r

def guessNumber(guess):
    global i
    if guess == correct_number:
        i = 0
        return "you win"
    else:
        if guess > correct_number:
            return "you entered bigger than correct number"
        else:
            return "you entered lower than correct number"

start = int(input("enter start number: "))
end = int(input("enter end number: "))
if start < end:
    correct_number = r.randint(start, end)
else:
    correct_number = r.randint(end, start)

i = 5
while i > 0:
    num = int(input(f"enter your chance {i}: "))
    print(guessNumber(num))
    i -= 1
else:
    print("you lose")
