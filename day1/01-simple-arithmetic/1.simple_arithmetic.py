num1: float = float(input("enter 1st number : "))
num2: float = float(input("enter 2nd number : "))
operator = input("Enter an operator(+ , - , * , / ) : ")
result: float
if(operator == '+'):
  result = num1+num2
elif(operator == '-'):
  result = num1-num2
elif(operator == '*'):
  result = num1*num2
elif(operator == '/'):
  result = num1/num2
else:
  print(f"{operator} : is not valid\n")

print(f"the result of num1({num1}) {operator} num2({num2}) : {result:.2f}\n")

