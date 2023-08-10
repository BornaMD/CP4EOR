a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []
div = int(input("Please provide with the number the list has to be devided by"))
#div = 2
def evenornot(a,div):
  for i in range(len(a)):
    if a[i]%div==0:
      b.append(a[i])
      i+=1
    else: 
      continue
  print(b)

evenornot(a,div)
