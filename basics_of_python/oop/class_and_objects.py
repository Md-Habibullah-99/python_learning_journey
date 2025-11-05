class Student:
  name = "Bro"
  id = 1597534826
  cgpa = 3.59
  def info(self):
    print(f"Name: {self.name}\nId: {self.id}\nCGPA: {self.cgpa}")

class Person():
  
  # constructor
  def __init__(self,name,age,occupation):
    self.name = name
    self.age = age
    self.ocupation = occupation
  '''def __init__(self):
    self.name = "abc"
    self.age = 0
    self.ocupation = "SD"
    '''
  def info(self):
    print(f"Name: {self.name} \nage: {self.age} \nOcupation: {self.ocupation}")
  

st1 = Student()
print(st1.name)
st1.info()
person1 = Person("Bro",15,"Student")
person1.info()
# person2 = Person()
# print(person2.name, person2.age, person2.ocupation)