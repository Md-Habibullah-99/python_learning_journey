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

st1 = Student()
print(st1.name)
st1.info()
preson1 = Person("Bro",15,"Student")
print(preson1.name)
print(preson1.age)
print(preson1.ocupation)