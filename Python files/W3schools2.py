import numpy as np

# Input variables
i = int(input("put in the number for a: "))
j = int(input("put in the number for b: "))
k = int(input("put in the number for c: "))
l = int(input("put in the number for n: "))

# Arrays
cars = ["Ford", "Volvo", "BMW"] 
cars.append("Toyota")
cars.append("Honda") 

# Functions using lambda

c = lambda a, b : a * b
x = lambda a, b, c : a + b + c
# Lambda Defenitions

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(int(input(l)))
mytripler = myfunc(3)

# Calling functions using parameters
print(x(i, j, k)) 
print(c(i,j)) 
print(mydoubler(i))
print(mytripler(i))

for Y in cars:
  print(Y) 

# Iteration
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# Stopiteration

class MyNumber:
  def __iter__(self):
    self.t = 1
    return self

  def __next__(self):
    if self.t <= 20:
      r = self.t
      self.t += 1
      return r
    else:
      raise StopIteration

myclas = MyNumber()
myiters = iter(myclas)

for r in myiters:
  print(r)

# Modules
# 1) Save a function / definition / program as .py
# 2) Import module_name as Nickname
# Syntax: module_name.function_name. etc. 
# or Syntax: Nickname.function_name. etc.
# or use from module_name import function_name
# and then just use the function. 

import datetime

f = datetime.datetime.now()
print(f.year)
print(f.strftime("%A")) 
