#Project 2 Guessing Game

import random #Import the random module

def guessing_game():
    print("Welcome to the Guessing Game!")
    
    while True:
        try:
            low = int(input("Enter the low number in the range: ")) #Ask for the low number in the range
            high = int(input("Enter the high number in the range: ")) #Ask for the high number in the range
            if low >= high:
                print("The lower number must be less than the higher number. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue
        
        random_number = random.randint(low, high) #Generate a random number within the selected range
        guesses = []
        attempts = 0
        
        while True:
            try:
                guess = int(input(f"Guess a number between {low} and {high}: ")) #Ask the user tio guess a number
                if guess in guesses:
                    print("You already guessed that number. Try again.") #Handles repeated guesses
                    continue
                if guess < low or guess > high:
                    print("Invalid guess. Please guess a number within the range.") #Handle out-of-range guesses
                    continue
                
                guesses.append(guess)
                attempts += 1
                
                if guess < random_number:
                    print("Too low Guess higher.") #Provide feedback for too-low guesses
                elif guess > random_number:
                    print("Too high Guess lower.") #Provide feedback for too-high guesses
                else:
                    print(f"Congratulations! You guessed the correct number in {attempts} tries.") #Congratulate the user on correct guesses
                    
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.") #Handle non-numeric inputs
            
        play_again = input("Do yout want to play again? (y/n):").lower() #Ask the user to play again
        if play_again != 'y':
            print("Thank you for playing Goodbye.")
            break
guessing_game()

        