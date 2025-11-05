class Employee:
  compay = "Brain station"
  
  def __init__(self, name, company, salary):
    self.name = name
    self.compay = company
    self.salary = salary
  def show(self):
    print(f"The name is {self.name} and company is {self.compay} and salary : {self.salary}")
  
  
  #class method as constructor
  @classmethod
  def fromStr(this, str):
    nst = str.split("-")
    return this(nst[0], nst[1], nst[2])
  
st = "abc-Zeron-12500"

print()
e1 = Employee.fromStr(st)
e1.show()
print(Employee.compay)

