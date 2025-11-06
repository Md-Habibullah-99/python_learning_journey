class Vector:
  def __init__(self,i,j,k):
    self.i = i
    self.j = j
    self.k = k
  
  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"
  
  # def __add__(self,x):
  #   return f"{self.i+x.i}i + {self.j+x.j}j + {self.k+x.k}k" #it should return string
  def __add__(self,x):
    return Vector(self.i+x.i, self.j+x.j , self.k+x.k) #now it should return Vector


v1 = Vector(1,2,3)
print(v1)
v2 = Vector(4,5,6)
print(v2)

print(v1 + v2)
print(type(v1+v2))