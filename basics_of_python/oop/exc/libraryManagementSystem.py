class Library:
  def __init__(self):
    self.numBooks = 0
    self.books = []
  def addBook(self,name):
    self.numBooks+=1
    self.books.append(name)
  def totalBooks(self):
    print(self.numBooks)
  def showBooks(self):
    for i in self.books:
      print(f"'{i}'",end=" ")
    print()

lb = Library()
lb.totalBooks()
lb.showBooks()
lb.addBook("Amar fashi chai")
lb.addBook("The chrossing")
lb.addBook("Ekus sotoker agenda")
lb.addBook("Karagarer rat din")
lb.totalBooks()
lb.showBooks()

