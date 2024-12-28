import random

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "draw"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "player"
    else:
        return "computer"

# Main game logic
def play_game():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("First to 5 points wins. Good luck!")

    while player_score < 5 and computer_score < 5:
        print("\nChoices: rock, paper, scissors")
        player_choice = input("Enter your choice: ").strip().lower()
        if player_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        if result == "player":
            player_score += 1
            print("You win this round!")
        elif result == "computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a draw!")

        print(f"Scores -> Player: {player_score}, Computer: {computer_score}")

    if player_score == 5:
        print("\nCongratulations! You won the match!")
    else:
        print("\nComputer won the match. Better luck next time!")

# Run the game
if __name__ == "__main__":
    play_game()