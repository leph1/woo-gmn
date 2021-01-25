import random

my_number = random.randint(1,100)
your_number = int(input("Guess my number (hint - it's an integer between 1 and 100): "))

while your_number != my_number:
    if your_number < my_number:
        your_number = int(input("Your guess is too low, try again: "))
    elif your_number > my_number:
        your_number = int(input("Your guess is too high, try again: "))
else:
    print("That's amazing! I really was thinking of the number "+str(my_number))
