#learning more about python lists

# nums = [i for i in range(1,11) if i > 5]
# print(nums)

# sq = [x*x for x in range(1,10)]
# print(sq)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist) 

newList = [x for x in fruits if "a" in x]
print(newList)

newList.sort(reverse = True)
print(newList)
