import os
import requests
import json

def generate_news():
  news_type = input("Enter the news type(eng: tesla, bitcoin, samsung, politics etc): ")

  url = f"https://newsapi.org/v2/everything?q={news_type}&from=2025-10-09&sortBy=publishedAt&apiKey=377b656dd442486b918cfcdc88be39c7"


  response = json.loads(requests.get(url).text)

  if os.path.exists("temp.json"):
    with open("temp.json", "w") as f:
      json.dump(response, f, indent=2)
  else:
    with open("temp.json", "x") as f:
      json.dump(response, f, indent=2)
  print()

