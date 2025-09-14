from comp import convert_input_to_num
from comp import compare
from computer_move import computer_move_func

print('''Moves are: 
r/R/0 = Rock
p/P/1 = Paper
s/S/2 = Scissors
      
to exit enter q/Q
''')
while True:
  user_input = input("Enter your move: ")
  if user_input == 'q' or user_input == 'Q':break
  if user_input == None:
    print('Invalid input')
    continue
  else:
    print(compare(convert_input_to_num(user_input),computer_move_func()))
