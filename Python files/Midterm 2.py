#Week 4
#Exercise 11
from functools import lru_cache
L = [7, 3, 5]

def middle(inputList):
  inputList = sorted(inputList)
  n = len(inputList)
  m = n - 1
  output = (inputList[int(n/2)] + inputList[int(m/2)]) / 2.0
  return output

print(middle(L))

#Exercise 12

width = 80
def center(s, width):
  if width < len(s):
    return s
  spaces = (width - len(s)) // 2
  result = " "* spaces+s
  return result

print(center("Some random stuff", width))
print(center("by some random company:", width))
print(center("Solving some random problem", width))
print("\n")
print(center("Copying some random stuff...", width))

# Exercise 13



# Exercise 18

#Exercise 18

string=""
def palindrome(string):
  string = string.lower()
  if(string==string[::-1]):
    return string + " is a palindrome"
  else:
    return string + " isn't a palindrome"

print(palindrome("issiNniSsi"))
# Exercise 19
def is_even_num(l):
  enum = []
  for n in l:
    if n % 2 == 0:
      enum.append(n)
  return enum
print (is_even_num([1, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]))

# Exercise 20
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

for i in range(1,1000):
  print(test_prime(i))


# Excersise 25

def pascal_triangle(n):
  trow = [1]
  y = [0]
  for x in range(max(n,0)):
    print(trow)
    trow = [1+r for n, r in x(trow+y, y+trow)]
  return n>=1
    
pascal_triangle(6)



#PAH08
def longest_word(filename):
  with open(filename, 'r') as infile:
    words = infile.read().split()
  max_len = len(max(words, key=len))
  return [word for word in words if len(word) == max_len]

print(longest_word('test.txt'))

def longest_word(filename):
  with open(filename, 'r+') as infile:
    words = infile.read().split()
  max_len = len(max(words, key=len))
  return [word for word in words if len(word) == max_len]

print(longest_word('test.txt'))

#21
import calendar

def isMagicDate(day, month, year):
  if day*month == year % 100:
    return True
  return False

def newf():
  for year in range (1900, 2000):
    for month in range (1,13):
      for day in range(1, calendar.monthrange(year,month)[1] + 1):
        if isMagicDate(day, month, year):
          print("%02d/%02d/%04d is a magic date." %(day, month, year))
                  
newf()
             
#
