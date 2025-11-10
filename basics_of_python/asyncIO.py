import time
import asyncio
import requests


async def func1():
  # time.sleep(3)
  await asyncio.sleep(2)
  print("func1")
  return "f1"
async def func2():
  # time.sleep(3)
  await asyncio.sleep(1)
  print("func2")
async def func3():
  # time.sleep(3)
  await asyncio.sleep(2)
  print("func3")
async def main():
  # task = asyncio.create_task(func1())
  # await func2()
  # await func3()
  #  this much faster then using await func() ->
  L = await asyncio.gather(
    func1(),
    func2(),
    func3()
  )
  print(L)

# asyncio.run(main()) #run main



async def download1():
  await asyncio.sleep(2)
  url = "https://4kwallpapers.com/images/wallpapers/windows-11-light-3840x2160-24447.png"
  response = requests.get(url)
  open("wallpaper1..png","wb").write(response.content)
  print("d01")
  return "d01"
async def download2():
  await asyncio.sleep(2)
  url = "https://4kwallpapers.com/images/wallpapers/windows-11-light-3840x2160-24447.png"
  response = requests.get(url)
  open("wallpaper2..png","wb").write(response.content)
  print("d01")
  return "d01"
async def download3():
  await asyncio.sleep(2)
  url = "https://4kwallpapers.com/images/wallpapers/windows-11-light-3840x2160-24447.png"
  response = requests.get(url)
  open("wallpaper3..png","wb").write(response.content)
  print("d01")
  return "d01"


async def download():
    # await download1()
    # await download2()
    # await download3()
    #  this much faster then using await func()
  L = await asyncio.gather(
    download1(),
    download2(),
    download3()
  )
  print(L)

asyncio.run(download())

