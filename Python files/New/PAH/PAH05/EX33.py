
a = int(input("Please provide with the number that needs to be devided by numbers: "))
b = []
def divisors(a):
  for i in range(1,a):
    if (a%i):
      b.append(i)
      i+=1
    else: 
      continue
  print(b)
  
for i in range(1,20):
  a=i
  print(divisors(a))


