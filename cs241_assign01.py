#Angus Macapella Assignment Guessing Game
import random
print("Welcome to the number guessing game!")

the_seed_value = input("Enter random seed: ")
print()
random.seed(the_seed_value)


def gameNum():
    num = random.randint(1,100)
    attempt = 1
    
    while attempt > 0:
        guess = int(input("Please enter a guess: "))
        
        if guess > num:
            print("Lower\n")
            
        elif guess < num:
            print("Higher\n")
            
        elif guess == num:
            print("Congratulations. You guessed it!\nIt took you " + str(attempt) + " guesses.\n")
            
            break
        attempt += 1
        
gameNum()

while True:
    again = input("Would you like to play again (yes/no)? ")
    if again == "yes":
        print()
        gameNum()
    else:
        print("Thank you. Goodbye.")
        break