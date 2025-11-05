def greet(fx):
  def mfx(*args, **kwargs):
    print("Good morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx

@greet
def hello():
  print("hello world")

def add(a,b):
  print(a+b)

hello()

greet(add)(1,2) #same as adding @greet
