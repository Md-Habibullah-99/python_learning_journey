s = set()
a = {1,2}
# print(type(s),s)
# print(a)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = {5,6,3,7,8,9}
print(s1.union(s2.union(s3)))
print(s1.intersection(s2.intersection(s3)))