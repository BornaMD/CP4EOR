a = list(input("Please provide a list: "))
b = list(input("Please provide another list: "))
c=[]

for i in a:
  if i in b:
    if i not in c:
      c.append(i)

print (c)