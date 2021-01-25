import random

low_num = int(input("Set the game parameters, enter the lowest number: "))
high_num = int(input("Now enter the highest number: "))
my_number = random.randint(low_num,high_num)
your_number = int(input("Guess my number (hint - it's an integer between "+str(low_num)+" and "+str(high_num)+"): "))
guess_count = 0

while your_number != my_number:
    if your_number < my_number:
        guess_count +=1
        your_number = int(input("Your guess is too low, try again: "))
    elif your_number > my_number:
        guess_count +=1
        your_number = int(input("Your guess is too high, try again: "))
else:
    guess_count +=1
    print("That's amazing! I really was thinking of the number "+str(my_number))
print("...And it only took you a measly "+str(guess_count)+" goes!")
