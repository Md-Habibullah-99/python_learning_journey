import time

# t = int(time.strftime('%H'))
t = 10
print(t)

if((t>20 and t<=24) or t<3):
  print("Good night!")
elif(t>=17):
  print("Good evining!")
elif(t>=15):
  print("Good noon!")
elif(t>=11):
  print("Good after noon!")
elif(t>3 and t<11):
  print("Good morning!")
