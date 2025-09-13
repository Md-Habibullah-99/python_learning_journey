dic = {"name":"hbh",
       "id":99}

# for i in dic:
#   print(i)

# for i in dic:
#   print(dic[i])

# for i in dic.keys():
#   print(f"The value corresponding to the keys ({i}): {dic[i]}")

# for key, value in dic.items():
#   print(f"The value corresponding to the keys ({key}): {value}")

ep1 = {111:50,222:90,333:58}
ep2 = {000:50,555:90,444:58}
print("ep1: ",ep1)
print("ep2: ",ep2)
ep1.update(ep2)
print("ep1: ",ep1)
print("ep2: ",ep2)
