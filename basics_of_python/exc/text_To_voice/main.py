import pyttsx3

engine = pyttsx3.init()

sayToThem = ["Alis", "My Bro", "Who"]

for i in sayToThem:
  engine.say(f"shout out to {i}")
  engine.runAndWait()
engine.say(f"What is shout out")
engine.runAndWait()
  

