def rev(a):
  if (a==0):
    return
  print(a)
  rev(a-1)
# rev(10)

def fac(n):
  if(n==1):
    return 1
  return n*fac(n-1)
# print(fac(5))

# def fib(n):
#   if(n<=0):
#     return 0
#   return fib(n-1)+fib(n-2)
# print(fib(5))