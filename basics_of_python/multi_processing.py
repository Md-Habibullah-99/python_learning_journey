import multiprocessing
import requests
import os
import concurrent.futures

def downloadFile(url, name):
  print(f"start downloading {name}")
  response = requests.get(url)
  open(f"{name}","wb").write(response.content)
  print(f"finish downladed {name}")

url_random = "https://lipsum.app/random/1600x900"
urls = [
  "https://4kwallpapers.com/images/wallpapers/windows-11-light-3840x2160-24447.png", 
  "https://4kwallpapers.com/images/wallpapers/mountain-landscape-3840x2160-24317.jpg", 
  "https://4kwallpapers.com/images/wallpapers/winter-mountain-3840x2160-24311.jpg", 
  "https://4kwallpapers.com/images/wallpapers/night-starry-sky-forest-silhouette-astronomy-cosmos-5k-3840x2160-1679.jpg"
  ]


pros = []
for url in urls:
  # normal download
  # downloadFile(url, os.path.basename(url))
  # multi processing
  p = multiprocessing.Process(target=downloadFile, args=[url, f"temp2/{os.path.basename(url)}"])
  p.start()
  pros.append(p)

for p in pros:
  p.join()


'''
# dont try this at home
with concurrent.futures.ProcessPoolExecutor() as executor:
  l1 = [url_random for i in range(60)]
  l2 = [i for i in range(60)]
  results = executor.map(downloadFile, l1, l2)
  for r in results:
    print(r)
'''

