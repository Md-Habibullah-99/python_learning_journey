#in python there is no concept like privet or protected, everything is public
class Employee:
  def __init__(self):
    self.__name = "abc"

a = Employee()
# print(a.__name) #cannot be accessed directly
print(a._Employee__name) #can be accessed indirectly (this is called "name mangling")

print("\n\n")

class Student:
  def __init__(self):
    self._name = "def"
  def _funName(self):
    return f"this is protected name : {self._name}"
  def show(self):
    print(self._funName())

s = Student()
s.show()
print("\n\n")


