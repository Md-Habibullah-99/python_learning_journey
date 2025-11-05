import os


for i in range(1,100):
  with open(f"./{i*5+10*9}.txt", "x") as f:
    f.close()


crDir = "./"
# if( not os.path.exists("./temp/*")):
#   crDir = "./temp/"

for i in range(100):
  os.rename(os.listdir(crDir)[i] , f"{i}.txt")
print(os.listdir(crDir))


