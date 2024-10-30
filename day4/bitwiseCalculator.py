import os
def bitwise_and(a: int,b: int) -> int:
  return a & b

def bitwise_or(a: int,b: int) -> int:
  return a  | b

def bitwise_xor(a, b) -> int:
  return a ^ b

def bitwise_not(a: int) -> int:
  return ~a & 0xFFFFFFFF

def left_shift(a, shift_by):
  return a << shift_by

def right_shift(a, shift_by):
  return a >> shift_by

def set_bit(num: int, bit_position: int) -> int:
  return num | (1 << bit_position)

def reset_bit(num: int, bit_position: int) -> int:
  return num & ~(1 << bit_position)

def toggle_bit(num: int,bit_position: int) -> int:
  return num ^ (1 << bit_position) # made mistake here earlier review twice while reading 

def convert_input(num_str: str) -> int:
  if num_str.startswith("0b"):
    return int(num_str,2) # binary to base 10(int)
  elif num_str.startswith("0x"):
    return int(num_str,16) # hexa to base 10(int)
  else:
    return int(num_str)


#func to get user input
def get_user_input() -> tuple[int,int]:
  # Get the first number
  num_str = input("Enter the number (prefix with 0b for binary, 0x for hexadecimal): ")
  num = convert_input(num_str)
  
  return num


def display_result(num1: int,num2: int) -> None:
  
  print(f"\nResults for numbers: {num1} and {num2}")
  print(f"{num1} AND {num2} = {bitwise_and(num1, num2)} (Decimal), {bin(bitwise_and(num1, num2))} (Binary), {hex(bitwise_and(num1, num2))} (Hexadecimal)")
  print(f"{num1} OR {num2} = {bitwise_or(num1, num2)} (Decimal), {bin(bitwise_or(num1, num2))} (Binary), {hex(bitwise_or(num1, num2))} (Hexadecimal)")
  print(f"{num1} XOR {num2} = {bitwise_xor(num1, num2)} (Decimal), {bin(bitwise_xor(num1, num2))} (Binary), {hex(bitwise_xor(num1, num2))} (Hexadecimal)")
  print(f"NOT {num1} = {bitwise_not(num1)} (Decimal), {bin(bitwise_not(num1))} (Binary), {hex(bitwise_not(num1))} (Hexadecimal)")
  print(f"Left Shift {num1} by 1 = {left_shift(num1, 1)} (Decimal), {bin(left_shift(num1, 1))} (Binary), {hex(left_shift(num1, 1))} (Hexadecimal)")
  print(f"Right Shift {num1} by 1 = {right_shift(num1, 1)} (Decimal), {bin(right_shift(num1, 1))} (Binary), {hex(right_shift(num1, 1))} (Hexadecimal)\n")

  # Bit Operations
  bit_position = int(input("Enter the bit position (0-indexed) to set/reset: "))
  print(f"Setting bit {bit_position} of {num1} = {set_bit(num1, bit_position)} (Decimal), {bin(set_bit(num1, bit_position))} (Binary), {hex(set_bit(num1, bit_position))} (Hexadecimal)")
  print(f"Setting bit {bit_position} of {num2} = {set_bit(num2, bit_position)} (Decimal), {bin(set_bit(num2, bit_position))} (Binary), {hex(set_bit(num1, bit_position))} (Hexadecimal)")

  print(f"Resetting bit {bit_position} of {num1} = {reset_bit(num1, bit_position)} (Decimal), {bin(reset_bit(num1, bit_position))} (Binary), {hex(reset_bit(num1, bit_position))} (Hexadecimal)")
  print(f"Resetting bit {bit_position} of {num2} = {reset_bit(num2, bit_position)} (Decimal), {bin(reset_bit(num2, bit_position))} (Binary), {hex(reset_bit(num2, bit_position))} (Hexadecimal)")
  
  print(f"Toggling bit {bit_position} of {num1} = {toggle_bit(num1, bit_position)} (Decimal), {bin(toggle_bit(num1, bit_position))} (Binary), {hex(toggle_bit(num1, bit_position))} (Hexadecimal)")
  print(f"Toggling bit {bit_position} of {num2} = {toggle_bit(num1, bit_position)} (Decimal), {bin(toggle_bit(num2, bit_position))} (Binary), {hex(toggle_bit(num2, bit_position))} (Hexadecimal)")
  

if __name__ == "__main__":
  os.system('clear') #use 'cls': argument for windows
  a = get_user_input()
  b = get_user_input()
  display_result(num1= a,num2 = b) # here num1,num2 : formal parameters   and a,b : actual parameters/values/arguments