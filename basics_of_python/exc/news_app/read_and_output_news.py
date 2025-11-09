import json


def read_and_generate():
  try:
    with open("temp.json","r") as f:
      data = json.load(f)
      for i in range(len(data["articles"])):
        print("Title: ",data["articles"][i]["title"])
        print("Description: ",data["articles"][i]["description"])
        print("Url: ",data["articles"][i]["url"], "\n")
  except json.JSONDecodeError as e:
    print("Error decoding JSON: ", e)
  
