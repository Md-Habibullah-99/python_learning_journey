
file_name = 'note.txt'

with open(file_name,'w') as f:
  f.write('')


with open(file_name,'r') as file:
  while True:
    uinput = input("Enter your input (n = write note, v = veiw note, d = delete a note, q to exit the program): ")
    if uinput == 'n' or uinput=='N':
      while True:
        note_input_from_user = input("Enter your note here")
        if not note_input_from_user:
          print("invalid input")
          continue
        else:
                    
          with open(file_name,'a') as write_note:
            write_note.write(note_input_from_user)
          break
        
    elif uinput == 'q' or uinput=='Q':
      break
    else :
      print("Invalid input")
    with open(file_name,'r') as t:
      print("note :",t.read())
    


