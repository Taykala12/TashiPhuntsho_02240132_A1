import random
# Function for the Guess the Number Game
def guess_number_game():
    lower= 1
    upper = 100
    number_to_guess = random.randint(lower, upper)
    
    print(f"Welcome to the Guess the Number Game!")
    print(f"Guess the number between {lower} and {upper}.")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            
            if user_guess < lower or user_guess > upper:
                print(f"Please guess a number between {lower} and {upper}.")
                continue
            
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number: {number_to_guess}")
                break
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Function for the Rock, Paper, Scissors Game
def rock_paper_scissors_game():
    choices = ["rock", "paper", "scissors"]

    print("Welcome to Rock, Paper, Scissors!")
    print("Choose 'rock', 'paper', or 'scissors'.")

    while True:
        user_choice = input("Enter your choice: ").lower()
        
        if user_choice not in choices:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("TIE!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win this round!")
        else:
            print("You lose this round!")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Main menu function
def main_menu():
    while True:
        print("\n--- Game Menu ---")
        print("1. Guess the Number Game")
        print("2. Rock, Paper, Scissors Game")
        print("3. Exit")
        
        choice = input("Choose a game (1/2/3): ")

        if choice == '1':
            guess_number_game()
        elif choice == '2':
            rock_paper_scissors_game()
        elif choice == '3':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
        choice = input("do you want to continue with functions (yes/no) : ")
        if choice != 'yes':
            print("EXITING")
            break
        
# Start the game with the main menu
if __name__ == "__main__" : 
    main_menu()