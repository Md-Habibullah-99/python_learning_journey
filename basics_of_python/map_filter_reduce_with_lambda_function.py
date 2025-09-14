def squre(n):
  return n**2


# MAP
l = [1,2,3,4,5,6,7,8,9]
l = list(map(squre,l))
print(l)

# FILTER
l = [1,2,3,4,5,6,7,8,9]
l = list(filter(lambda n:n>3,l))
print(l)

# REDUCE
from functools import reduce
l = [1,2,3,4,5,6,7,8,9]
sum = reduce(lambda x,y: x+y, l)
print(sum)

