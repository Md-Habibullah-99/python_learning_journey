def kbcfunc():
  qls = ["What is the name of capital of Bangladesh?",
        "What is the name of capital of India?",
        "What is the name of capital of Pakistan?",
        "Are Russia and Ukrian friend?",
        "Who are you?"]
  als = ["Dhaka","New Delhi","Islamabad","No","Who am I?"]
  opls = [
    ["Dhaka","New Delhi","Islamabad","Biejing"],
    ["Dhaka","New Delhi","Islamabad","Biejing"],
    ["Dhaka","New Delhi","Islamabad","Biejing"],
    ["Very good friend","No","Yes","Russia is not a country"],
    ["Kim jong un","Ossama bin laden","Barak obama","Who am I?"]
    ]
  pls = [1000,10000,100000,1000000,10000000]
  bal = 0
  a = 0
  for q in qls:
    print("Question ", a+1," for ",pls[a],": ")
    print(q)
    b = 0
    for i in opls[a]:
      b=b+1
      print(b,i)
    ans = int(input("Enter the right answer: "))
    if ans>4 or ans<1 : 
      print("Wrong ans!")
      print("Your final balance is: ",bal)
      break
    if opls[a][ans-1] == als[a]:
      bal = bal + pls[a]
      print("Currect ans! \n ")
    else: 
      print("Wrong ans!")
      print("Your final balance is: ",bal)
      break
    a=a+1
  if bal == sum(pls):
    print("\n\n\nYour all answer was correct!\nYour final balance is: ",bal)
    print("\n\n\n\n")
kbcfunc()