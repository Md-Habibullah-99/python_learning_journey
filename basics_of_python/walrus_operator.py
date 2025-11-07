# assigns values to variables as part of a larger expression 

'''
n = [1,2,3,4,5]
while( a:= len(n)) > 0:
  print(n.pop())

print("len of n :", len(n))'''

'''
f = False
print(f)
print(f:=True)
'''

foods = list()
'''# without walrus operator
while True:
  food = input("What food do you like?: ")
  if food == "quit":
    break
  foods.append(food)
'''
'''
# with walrus operator
while (food := input("What food do you like?: ")) != "quit":
  foods.append(food)
'''

