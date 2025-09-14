def convert_input_to_num(x):
  if x=='r' or x=='R' or x=='1':
    return 1
  elif x=='p' or x=='P' or x=='2':
    return 2
  elif x=='s' or x=='S' or x=='3':
    return 3
  else :return None



def compare(u,c):
  if u==c:
    return 'tie'
  elif u == 2:
    if c == 3:
      return 'lose'
    else:
      return 'win'
  elif u == 1:
    if c == 2:
      return 'win'
    else:
      return 'lose'
  elif u == 3:
    if c == 1:
      return 'lose'
    else:
      return 'win'
  else:
    return 'Invalid move'

