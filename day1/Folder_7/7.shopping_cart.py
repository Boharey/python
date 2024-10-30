foods: list[str] = list()
prices: dict[str,int] = {
    "Apple": 1.20,
    "Banana": 0.50,
    "Bread": 2.50,
    "Cheese": 3.75,
    "Chicken": 5.00,
    "Coffee": 4.00,
    "Eggs": 2.20,
    "Ice Cream": 3.50,
    "Milk": 1.80,
    "Orange": 0.80,
    "Pasta": 1.90,
    "Pizza": 8.50,
    "Rice": 1.30,
    "Salmon": 7.00,
    "Steak": 10.00,
    "Tomato": 0.90,
    "Yogurt": 1.00
}

total: int = 0

while True:
  food = input("enter item to buy or (q or Q to quit) : ") 
  if(food.lower() == 'q'):
    break
  else:
    foods.append(food)
    total += prices[food]

for food in foods:
  print(food,end= " ")
  print(prices[food])
print(total)