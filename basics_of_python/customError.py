"""
a = int(input("Enter a number between 5-9 : "))

if(a>9 or a<5):
  raise ValueError("Value should be between 5-9")
"""


while(True):
  q = input("Enter a number or quit to exit: ")
  if(q.lower() == "quit"):
    break
  try:
    q = int(q)
  except Exception as e:
    print(e)
  finally:
    print("Who are you?")
