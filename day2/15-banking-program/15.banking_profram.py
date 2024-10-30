#banking program
is_running: bool = True
balance: float = 0.0

def showBalance() -> None:
  global balance
  print(f"your balance is : {balance:.2f}")

def deposit() -> None:
  global balance  # Access the global balance variable
  amount = float(input("Enter the amount to deposit: $"))
  if amount > 0:
    balance += amount
    print(f"${amount:.2f} has been deposited. New balance: ${balance:.2f}")
  else:
    print("Invalid deposit amount. Please enter a positive number.")


def withdraw():
  global balance  # Access the global balance variable
  amount = float(input("Enter the amount to withdraw: Rs: "))
  if amount > 0:
    if amount <= balance:
      balance -= amount
      print(f"${amount:.2f} has been withdrawn. New balance: ${balance:.2f}")
    else:
      print("Insufficient funds for this withdrawal.")
      
  else:
      print("Invalid withdrawal amount. Please enter a positive number.")



def handle_case(val) -> None:
  global is_running
  match val:
    case "1":
      showBalance()
    case "2":
      deposit()
    case "3":
      withdraw()
    case "4":
      #exit the program
      is_running = False
    case _:
      print("\ninvalid case: please check your value once again\n")
      
while is_running == True:
  print("Banking Program")
  print("1. Show Balance")
  print("2. Deposit")
  print("3. Withdraw")
  print("4. Exit")
  
  choice: str = input("Enter your choice : 1-4 : ")
  handle_case(choice)
  