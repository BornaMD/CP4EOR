# slide 7 

A = [int(x) for x in input("Put in the list: ").split()]
x = int(input("Put in the number to be checked: "))

def IsInlist(A,x):
  for i in range(len(A)):
    if A[i] == x:
      return True
  return False

print(IsInlist(A, x))

# slide 22

n = int(input("Put in the number to return its factorial: "))

def factltr(n):
  if n <= 0:
    raise Exception("Faculty does not exist.")
  
  y = 1
  for i in range(1,n+1):
    y = y*i
    i +=1
  return y

print(factltr(n))

# Always start with the part of the function that stops the loop, otherwise the loop will continue forever.

def fib(n):
    if n == 0:
        return 0
    else:
        return mult3(n-1) + 3

for i in range(1,10):
    print(mult3(i))

