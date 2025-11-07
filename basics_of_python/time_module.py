import time

def usingWhile():
  i = 0
  while i<10000000:
    a = i
    i+=1
def usingFor():
  for i in range(10000000):
    a = i

# t1 = time.time()
# usingFor()
# print("For: " ,time.time() - t1)
# t1 = time.time()
# usingWhile()
# print("While: ",time.time() - t1)

# print("Before 4 sec")
# time.sleep(4)
# print("After 4 sec")

# while (True):
#   print(time.time())

# while True:
#   t = time.localtime()
#   formated_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
#   print(formated_time)


