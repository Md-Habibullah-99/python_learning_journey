import os

if( not os.path.exists("temp")):
  os.rmdir("temp")

for i in range(1,100):
  # os.rmdir(f"temp/day{i}")
  os.mkdir(f"temp/day{i}")
