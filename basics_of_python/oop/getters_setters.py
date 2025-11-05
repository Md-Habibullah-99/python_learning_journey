class MyClass:
  def __init__(self,value):
    self._value = value
  def show(self):
    print(f"Value is: {self._value}")
  
  @property
  def value(self):
    return 10*self._value
  
  @value.setter
  def set_value(self,val):
    self._value = val

obj = MyClass(10)
obj.set_value = 5
print(obj.value)