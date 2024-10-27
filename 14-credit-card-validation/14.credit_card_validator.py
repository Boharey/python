def credit_card_validator(number: str) -> bool:
  #filtering the number to contain only numeric characters
  number = "".join(filter(str.isdigit,number))
  # print(number)
  reversed_number = number[::-1]
  # print(reversed_number)
  i: int = 0
  sum: int = 0
  for digit in reversed_number:
    digit = int(digit)

    #only for even i,e --> i%2 == 1:
    if(i & 1 == 1):
      
      # one liner
      # digit = digit*2 if digit<5 else digit*2 - 9 
      digit = digit * 2
      # Subtract 9 if the doubled value is greater than 9
      if digit > 9:
        digit -= 9     
    sum += digit
    i += 1 
  print(sum)   
  if sum%10 == 0:
    return True
  else:
    return False

print(credit_card_validator('1234-5678-9012-3456'))