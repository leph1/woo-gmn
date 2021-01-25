import random

# Check whether the input is an integer
def input_number(message):
    while True:
        try:
            user_input = int(input(message))       
        except ValueError as e:
            print(str(e)+" is not an integer! Please try again.")
            continue
        else:
            return user_input 
            break

# Check whether the number is higher and provide appropriate guidance
def high_num_check(message):
    while True:
        try:
            high_num = input_number(message) #Still need to check whether it's an integer as well!
            if low_num >= high_num:
                raise Exception("The upper boundary needs to be higher than the lower boundary! Please Try again.")
        except Exception as e:
            print(e)
            continue
        else:
            return high_num
            break

#variables
low_num = input_number("Set the game parameters, enter the lowest number: ")
high_num = high_num_check("Now enter the highest number: ")
my_number = random.randint(low_num,high_num) #grab a random number between the two bounds chosen by the user
your_number = input_number("Guess my number (hint - it's an integer between "+str(low_num)+" and "+str(high_num)+"): ") #Still need to check whether it's an integer as well!
guess_count = 0

#main game loop
while your_number != my_number:
    if not low_num <= your_number <= high_num:
        your_number = input_number("Your guess is out of bounds, Please enter a number between "+str(low_num)+" and "+str(high_num)+"): ")
        guess_count +=1
    elif your_number < my_number:
        guess_count +=1
        your_number = input_number("Your guess is too low, try again: ")
    elif your_number > my_number:
        guess_count +=1
        your_number = input_number("Your guess is too high, try again: ")
else:
    guess_count +=1
    print("That's amazing! I really was thinking of the number "+str(my_number))
print("...And it only took you a measly "+str(guess_count)+" guesses!")
