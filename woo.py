import random

low_num = int(input("Set the game parameters, enter the lowest number: "))
high_num = int(input("Now enter the highest number: "))
my_number = random.randint(low_num,high_num)
your_number = int(input("Guess my number (hint - it's an integer between "+str(low_num)+" and "+str(high_num)+": "))

while your_number != my_number:
    if your_number < my_number:
        your_number = int(input("Your guess is too low, try again: "))
    elif your_number > my_number:
        your_number = int(input("Your guess is too high, try again: "))
else:
    print("That's amazing! I really was thinking of the number "+str(my_number))
