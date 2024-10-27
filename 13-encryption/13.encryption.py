import string
import random

# Defining string containing all possible characters for encryption:
# letters (uppercase and lowercase), digits, whitespace, and punctuation.
chars: str = string.ascii_letters + string.digits + " " + string.punctuation

# Convert `chars` to a list for easy indexing and manipulation.
chars: list[str] = list(chars)


# Create a shuffled copy of `chars` to serve as the encryption key.
keys: list[str] = chars.copy()
random.shuffle(keys)  # Shuffle to create a unique mapping for encryption.

# Display the original characters and their shuffled counterparts (keys).
print(f"Characters: {chars}\n")
print(f"Keys: {keys}\n")

# Input from the user that will be encrypted.
plain_text: str = input("Enter text to encrypt: ")

# Initialize empty strings for the encrypted and decrypted messages.
encrypted: str = ""
decrypted: str = ""

def encrypt(text: str) -> str:
    """Encrypt the input text by substituting each character with its shuffled counterpart."""
    global encrypted
    encrypted = ""  # Clear the encrypted string for each call.
    for letter in plain_text:
        index = chars.index(letter)  # Find the index of the letter in `chars`.
        encrypted += keys[index]     # Use the index to find the corresponding letter in `keys`.
    return encrypted

def decrypt(text: str) -> str:
    """Decrypt the encrypted text by substituting each character back to its original counterpart."""
    global decrypted
    decrypted = ""  # Clear the decrypted string for each call.
    for letter in text:
        index = keys.index(letter)   # Find the index of the letter in `keys`.
        decrypted += chars[index]    # Use the index to find the original letter in `chars`.
    return decrypted

# Display the results: original text, encrypted text, and decrypted text.
print(f"Plain text: {plain_text}")
print(f"Encrypted text: {encrypt(plain_text)}")


print(f"Decrypted text: {decrypt(encrypted)}")


