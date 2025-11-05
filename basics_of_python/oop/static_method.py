class Math:
  def __init__(self,num):
    self.num = num

  def addToNum(self,n):
    self.num = self.num+n

  @staticmethod
  def add(a,b):
    return a+b

a = Math(5)
print(a.num)
a.addToNum(6)
print(a.num)
# using static method
print(a.add(1,2))
print(Math.add(1,2))