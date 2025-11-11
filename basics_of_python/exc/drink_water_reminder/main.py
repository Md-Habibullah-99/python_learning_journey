import os,time

def send_notification(min):
  
  title = f"{min}min"
  massage = f"You haven't drink water in {min}minutes"
  command = f'''
  notify-send "{massage}" "{title}"
  '''
  os.system(command)

def counter():
  i = 1
  while True:
    time.sleep(10*60)
    if(i%20==0):
      send_notification(20)
    i+=1
    
counter()

