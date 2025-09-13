marks = [56,31,58,98,65,45]

for index,mark in enumerate(marks):
  print(mark)
  if(index==3):
    print("Awesome")

for index,mark in enumerate(marks, start=1):
  print(mark)
  if(index==3):
    print("Awesome")