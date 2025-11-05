class Employee:
  class_variable = 0 #class variable
  class_variable_company_name = "Brain station" #class variable

  def __init__(self,name):
    Employee.class_variable +=1
    self.name = name #this is instance variable
  def print_class_variable(self):
    print(Employee.class_variable)
  def companyName(self):
    print(f"{self.name}s company: {self.class_variable_company_name}")


a = Employee("abc")
b = Employee("def")
'''print(a.class_variable)
a.print_class_variable()
print(b.class_variable)
b.print_class_variable()'''
a.class_variable_company_name = "Zeron"
a.companyName()
b.companyName()

#we can also do this:
print(Employee.class_variable_company_name)
Employee.class_variable_company_name = "Google"
c = Employee("lsd")
c.companyName()
