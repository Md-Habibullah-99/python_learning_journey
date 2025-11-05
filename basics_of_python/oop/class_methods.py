class Employee:
  compay = "Brain station"
  def show(self):
    print(f"The name is {self.name} and company is {self.compay}")
  
  @classmethod
  def changeCompany(cls, newCompany):
    cls.compay = newCompany
  

print()
e1 = Employee()
e1.name = "abc"
e1.show()
e1.changeCompany("Zeron")
e1.show()
print(Employee.compay)

