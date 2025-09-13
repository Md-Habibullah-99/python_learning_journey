f = open("t.txt","w")
name = "Bro"
f.write(f"Yo {name} whats up")
f.close() #must close the file
text = open('t.txt','r').read()
print(text)

#it works but not recomended
text = open('t.txt','a').write("abcd")
print(text)
text = open('t.txt','r').read()
print(text)

# if i use this  then i don't need to close the file
with open('t.txt','a') as t:
  t.write(" i am inside t.txt \nYo whats up")
text = open('t.txt','r')
print(text.read())
text.close()