class Student:
  def __init__(self,name,id):
    self.name = name
    self.id = id

  def details(self):
    print(f"The name of Student {self.id} is {self.name}")
    
class Employee(Student):
  def __init__(self, name, id, projects_number):
    super().__init__(name, id)
    self.projects_number = projects_number
  
  def details(self):
    print(f"The name of Employee {self.id} is {self.name}, and total projects: {self.projects_number}")
  


s1 = Student("abc",123)
s1.details()
e1 = Employee("def",456,5)
e1.details()