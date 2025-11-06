import os

#making the files
'''
if( not os.path.exists("./temp/*")):
  os.mkdir("./temp/")
for i in range(1,10000):
  if( not os.path.exists(f"./temp/{i*5+10*9+3*100}.txt")):
    with open(f"./temp/{i*5+10*9+3*100}.txt", "x") as f:
      f.close()
'''


crDir = "./temp/"
flist = os.listdir(crDir)

#renaming the files
i=0
for f in flist:
  os.rename(f"{crDir}/{f}" , f"{crDir}/{i}.txt")
  i+=1






