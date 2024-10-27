Text Encryption and Decryption in Python

This Python script performs simple text encryption and decryption using character substitution. It uses a random mapping of characters, where each character in the input text is replaced with a corresponding character from a shuffled version of the original character set.
Table of Contents

    Overview
    How It Works
    Setup
    Usage
    Sample Output
    Notes
    License

Overview

This project encrypts and decrypts text using character substitution with a randomly shuffled set of characters, including letters (uppercase and lowercase), digits, whitespace, and punctuation.
How It Works

    Character Set: A character set (chars) is defined with all letters, digits, spaces, and punctuation.

    Key Generation: A shuffled copy of chars (keys) is created to act as the encryption key.

    Encryption: The script iterates through the input text (plain_text), replacing each character with its corresponding value in keys based on its index in chars.

    Decryption: The process is reversed by mapping each character in the encrypted text back to the original text using chars and keys.

Setup
Prerequisites

    Python 3.x
    Standard libraries string and random (both included in Python by default)

Installation

Clone or download this repository to your local machine.
Usage

    Open a terminal and navigate to the script directory.

    Run the script:

    bash

    python encryption_script.py

    Enter the text you want to encrypt when prompted.

    The script will output the original text, the encrypted text, and the decrypted text.

Code Structure

    chars: A list of all characters that could be encrypted.
    keys: A shuffled version of chars to serve as the encryption key.
    encrypt(text: str) -> str: A function that encrypts the text.
    decrypt(text: str) -> str: A function that decrypts the text.

Sample Output

plaintext

Characters: ['a', 'b', 'c', ..., '?']
Keys: ['G', '7', 'b', ..., '#']

Enter text to encrypt: hello world

Plain text: hello world
Encrypted text: G7#Ioi%wA<$
Decrypted text: hello world

Notes

    Random Key: Since the keys list is shuffled each time the script runs, the encrypted result will be unique for each session.
    Security: This script is for educational purposes only and does not provide secure encryption suitable for sensitive information.

License

This project is open-source and available under the MIT License.