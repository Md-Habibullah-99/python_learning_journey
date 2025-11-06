class Employee:
  def __init__(self,name):
    self.name = name
  def __len__(self):
    # i = 0
    # for c in self.name:
    #   i = i+1
    return len(self.name)
  def __str__(self):
    return f"The name of the employee is {self.name} str"
  def __repr__(self):
    return f"The name of the employee is {self.name} repr"
  def __call__(self):
    print("This is call method")

e = Employee("Abc")
print(e.name)
print(len(e)) #we defined it as __len__ but we can call it len
print(e) #for __str__
# we can also do this:
print(str(e))
print(repr(e))
e() #call method