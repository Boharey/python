import random,os

# Use a tuple for storing options since it's immutable
options: tuple[str, ...] = ("rock", "paper", "scissor")

#clearing screen for better representation  
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# Initialize score variables
wins: int = 0
loss: int = 0
play_again: str = 'y'

while play_again == 'y':
    # AI makes a choice
    clear_screen()
    AI_choice: str = random.choice(options)
    
    # User makes a choice
    user_choice: str = input("Select your choice ('rock', 'paper', 'scissor'): ").lower()
    
    print(f"AI choice: {AI_choice}")
    print(f"User choice: {user_choice}")

    # Determine the outcome
    if AI_choice == user_choice:
        print("It's a draw!\n")
    elif (AI_choice == 'rock' and user_choice == 'paper') or \
         (AI_choice == 'paper' and user_choice == 'scissor') or \
         (AI_choice == 'scissor' and user_choice == 'rock'):
        print("User wins!")
        wins += 1
    else:
        print("User loses!")
        loss += 1

    print(f"Score: Wins({wins}), Loss({loss})\n")
    play_again = input("Wanna play again? (y) or (n): ").lower()

print(f"Final Score: Wins({wins}), Loss({loss})\n")
