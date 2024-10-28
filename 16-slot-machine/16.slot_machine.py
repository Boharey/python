import random

balance: float = float(input("Enter your total balance: "))
runGame: bool = True
gamesWon: int = 0
gamesLost: int = 0
emojis: list[str] = [
    "\U0001F604",  # 😄 Smiling Face with Open Mouth & Smiling Eyes
    "\U0001F923",  # 🤣 Rolling on the Floor Laughing
    "\U0001F62D",  # 😭 Loudly Crying Face
    "\U0001F61D",  # 😝 Squinting Face with Tongue
    "\U0001F44D",  # 👍 Thumbs Up
]

def play() -> None:
    global balance
    global gamesLost
    global gamesWon
    global runGame

    if balance < 10:
        print("Insufficient balance to play.\n")
        makeChoice = input("1. Add balance or 2. Exit game\n")
        
        match makeChoice:
            case "1":
                try:
                    add_balance = float(input("Add balance: "))
                    balance += add_balance
                    print(f"New balance: {balance}\n")
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    runGame = False
            case "2":
                runGame = False
                exit_game()
            case _:
                print("Invalid input, exiting game.")
                runGame = False
                exit_game()
        return
    
    balance -= 10
    slot1: str = random.choice(emojis)
    slot2: str = random.choice(emojis)
    slot3: str = random.choice(emojis)
    
    # Display the slots result
    print(f"Slots: {slot1} | {slot2} | {slot3}")

    if slot1 == slot2 == slot3:
        balance += 100
        gamesWon += 1
        print(f"You won! Your new balance is: {balance}\n")
    else:
        gamesLost += 1
        print(f"You lost. Your remaining balance is: {balance}\n") 

def exit_game() -> None:
    global runGame
    print(f"Your final balance is: {balance:.2f}")
    print(f"You won: {gamesWon} games and lost: {gamesLost} games")
    runGame = False
   
while runGame:
    print("Welcome to the slot machine game!")
    print("Symbols: 😄, 🤣, 😭, 😝, 👍")
    print("Each game costs Rs 10. Win by matching all three slots!")
    print("Please make a choice:")
    choice: str = input("1. Play.\t2. Exit\n")
    match choice:
        case "1":
            play()
        case "2":
            exit_game()
        case _:
            print("\nInvalid choice! Please select either 1 or 2.\n")
