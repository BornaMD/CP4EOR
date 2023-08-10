from functools import lru_cache

@lru_cache(1000)
def pascal(n):
  if n==1:
    return [1]
  else:
    line=[1]
    previous_line=pascal(n-1)
    for i in range(len(previous_line)-1):
      line.append(previous_line[i]+previous_line[i+1])
    line+=[1]
  return line

for i in range(1,20):
  print(pascal(i))

@lru_cache(maxsize=1000)
def test_prime(n):
  if (n==1):
    return False
  elif (n==2):
    return True
  else:
    for x in range(2,n):
      if (n % x==0):
        return False
    return True

for i in range(1,10):
  print(test_prime(i))

width = 90
def centered(string, width):
  if width < len(string):
    return string
  spaces = (width - len(string)) //2
  return int" " * spaces + string

for i in range(1,20):
  print(centered(pascal(i),width))


print(centered("hello all of you there, I am doing weird stuff", width))

#import pydoc
#
#help()

#def pascal_triangle(n):
#  trow = [1]
#  y = [0]
#  for x in range(max(n,0)):
#    print(trow)
#    trow = [1+r for n, r in x(trow+y, y+trow)]
#  return n>=1
#
#for i in range(1,pascal_triangle(n=1)):
#  pascal_triangle(6)


#def palindrome(string):
#  string = string.lower()
#  if(string==string[::-1]):
#    return string + " is a palindrome"
#  else:
#    return string + " isn't a palindrome"
#
#print(palindrome("issiNniSsi"))

#def prime(givenNumber):  
#    
#    # Initialize a list
#    primes = []
#    for possiblePrime in range(2, givenNumber + 1):
#
#        # Assume number is prime until shown it is not. 
#        isPrime = True
#        for num in range(2, int(possiblePrime ** 0.5) + 1):
#            if possiblePrime % num == 0:
#                isPrime = False
#                break
#
#        if isPrime:
#            primes.append(possiblePrime)
#    
#    return(primes)
#
#print(prime(90))
#
#if num > 1:
#   # check for factors
#   for i in range(2,num):
#       if (num % i) == 0:
#           print(num,"is not a prime number")
#           print(i,"times",num//i,"is",num)
#           break
#   else:
#       print(num,"is a prime number")
#       
## if input number is less than
## or equal to 1, it is not prime
#else:
#   print(num,"is not a prime number")