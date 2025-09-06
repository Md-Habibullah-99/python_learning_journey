
"""
try:
  a = int(input("Enter a number: "))
  print(f"Multiplication table of {a}:")
  for i in range(a):
    print(f"{a}x{i}={a*i}")
# except Exception as e:
#   print(e)
except:
  print("Invalid input")
"""

"""
try:
  b=int(input("Enter a number:"))
except ValueError as e:
  print(e)
except IndexError:
  print("Index error")
finally:
  print("I am always executed")
print("I am always executed")
"""


def func1():
  try:
    b=int(input("Enter a number:"))
    return 0
  except ValueError as e:
    print(e)
    return 1
  except IndexError:
    print("Index error")
    return 1
  finally:
    print("I am always executed")
  print("I am always executed out of exception")
x = func1()
print(x)
