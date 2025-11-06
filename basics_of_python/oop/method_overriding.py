class Shape:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def area(self):
    return self.x*self.y

class Squre(Shape):
  def __init__(self, x, y):
    super().__init__(x,y)
  
  def area(self):
    print("The shape of squer is : ", self.x*self.y)

class Circle(Shape):
  def __init__(self, x):
    self.x = x
    super().__init__(x,x)
  
  def area(self):
    return 3.1416*super().area()

c = Circle(3)
print(c.area())


