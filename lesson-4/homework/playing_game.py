import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 10
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    
    while attempts > 0:
        try:
            guess = int(input(f"You have {attempts} attempts left. Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if guess > number_to_guess:
            print("Too high!")
        elif guess < number_to_guess:
            print("Too low!")
        else:
            print("You guessed it right!")
            break
        
        attempts -= 1
    
    if attempts == 0:
        print(f"You lost. The correct number was {number_to_guess}.")
    
    replay = input("Want to play again? (Y/YES/yes/ok): ").strip().lower()
    if replay in ['y', 'yes', 'ok']:
        play_game()
    else:
        print("Thanks for playing!")

# Start the game
play_game()