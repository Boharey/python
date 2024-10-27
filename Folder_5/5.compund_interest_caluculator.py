# compound interest calculator

principle: float = float(input("enter the principle : "))
rate: float = float(input("enter the rate : "))
time_in_years:float = float(input("enter the time_in_years : "))

while(principle <= 0 or rate <= 0 or time_in_years <= 0):
  print("invalid input in any one of the values")
  principle: float = float(input("enter the principle : "))
  rate: float = float(input("enter the rate : "))
  time_in_years:float = float(input("enter the time_in_years : "))

total: float = principle * pow(1 + rate/100,time_in_years)
print(f"{total:.2f}")
