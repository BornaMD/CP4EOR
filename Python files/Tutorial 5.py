# Exercise 7

n = int(input("Put in the number to return its factorial: "))

def factltr(n):
    if n == 1:
        return 1
    else:
        return factltr(n-1) * n 

print(factltr(n))

# Exercise 10

# sum_even(n): number -> number
# sum_even(n) is the sum of even numbers from 0 to N.
def sum_even(n):
    if n == 0:
        return 0
    elif n % 2 != 0:
        return sum_even(n-1)
    else:
        return sum_even(n-2) + n

print(sum_even(n))

# Exercise 13

Wo = str(input("Give me a word: "))

def ispalindrome(Wo):
    word = [c for c in Wo.lower() if c.isalpha()]
    if len(word) < 2:  
        return True
    if word[0] != word[-1]: 
        return False
    return ispalindrome(word[1:-1])

print(ispalindrome(Wo))


def pali(x):
  y = [ c for c in x.lower() if c.isalpha()]
  return (y == y[::-1])

#main
x = str(input("Enter a string: "))
boo = pali(x)
print ("the statement that "+"'"+x+"'"+" is a palindrome is ",boo)

# Excercise 14
def factorial(n):
   if n == 0:
       return 1
   else:
        returnNumber = n * factorial(n-1) 
        print(str(n) + '! = ' + str(returnNumber))
        return returnNumber

print(factorial(n))