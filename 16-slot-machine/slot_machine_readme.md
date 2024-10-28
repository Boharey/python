# Slot Machine Game 🎰

A simple slot machine game built in Python where players can test their luck by matching emoji symbols to win rewards. Each game costs Rs 10, and a winning spin multiplies the bet by 10. Players can add more funds if they run out of balance.

## Features
- Random emoji symbols on each spin.
- Win if all three emojis match, with a prize of Rs 100.
- Option to add more balance if it runs low.
- Game summary at the end, displaying games won and lost.

## Requirements
- Python 3.6 or later

## How to Play
1. Clone this repository or copy the code into your local Python environment.
2. Run the program:
    ```bash
    python slot_machine_game.py
    ```
3. Enter your initial balance when prompted.
4. Choose from the following options:
   - `1. Play`: Deducts Rs 10 from your balance and spins the slot machine.
   - `2. Exit`: Ends the game and shows your final balance and game statistics.
5. If your balance falls below Rs 10, you'll be given the option to add more funds or exit the game.

## Rules
- Each play costs Rs 10.
- Three identical emojis win a jackpot of Rs 100.
- Track games won and lost throughout the session.

## Example Usage
```plaintext
Welcome to the slot machine game!
Enter your total balance: 50
Symbols: 😄, 🤣, 😭, 😝, 👍
Each game costs Rs 10. Win by matching all three slots!

Please make a choice:
1. Play    2. Exit

## Sample Output
Slots: 😄 | 😄 | 😄
You won! Your new balance is: 140.0

Slots: 😝 | 🤣 | 😭
You lost. Your remaining balance is: 130.0
