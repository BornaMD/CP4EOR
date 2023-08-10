def max_no(x, y):
    if x > y:
        return x
    else:
        return y

i=2
j=3
print(max_no(i,j))

def ColorIndex(s):
    if(s.lower()=="blue"):
        return "first"
    elif (s.lower()=="white"):
        return "second"
    elif (s.lower()=="red"):
        return "third"
    else:
        return ""

s=input("Pick a color: blue, white, red? ")
order= ColorIndex(s)
if(order!=""):
    print("You picked the ", order, " color")
else:
    print("You did not pick from the list")    


def divisions(x,y):
    return x//2, y//2
i,j = 7,10
i,j=divisions(i,j)
print("i=", i," j=", j)

# //= is the same as // + == 
# Whenever you see simular code, that has other code in between them, use functions to make the mainanance easier. 
# In case there is no code in between the code patterns, use for loops. 

a1=int(input("Give the numerator of No. 1: "))
a2=int(input("Give the denominator of No. 1: "))
b1=int(input("Give the numerator of No. 2: "))
b2=int(input("Give the denominator of No. 2: "))

def gcd(x, y):
 while y != 0:
  (x, y) = (y, x % y)
 return x

def simplify (c1,c2):
 # calculate gcd for subtraction
 x=gcd (c1,c2)
 #divide by gcd
 c1 //= x
 c2 //= x
 return c1,c2


#add
c1=a1*b2+a2*b1
c2=a2*b2
c1,c2= simplify(c1,c2)
# print the result of summation
print("sum: " + str(c1)+ "/" +str(c2) )

#subtract
c1=a1*b2-a2*b1
c2=a2*b2
c1,c2= simplify(c1,c2)
# print the result of subtraction
print("subtraction: " + str(c1)+ "/" +str(c2) )

#multiplication
c1=a1*b1
c2=a2*b2
c1,c2= simplify(c1,c2)
# print the result of multiplication
print("multiplication: "+ str(c1)+ "/" +str(c2) )

#divide
c1=a1*b2
c2=a2*b1
c1,c2= simplify(c1,c2)
# print the result of division
print("division: "+ str(c1)+ "/" +str(c2) )

from mdlFraction import simplify

a1=int(input("Give the numerator of No. 1: "))
a2=int(input("Give the denominator of No. 1: "))
b1=int(input("Give the numerator of No. 2: "))
b2=int(input("Give the denominator of No. 2: "))

#add
c1=a1*b2+a2*b1
c2=a2*b2
c1,c2= simplify(c1,c2)
# print the result of summation
print("sum: " + str(c1)+ "/" +str(c2) )

#subtract
c1=a1*b2-a2*b1
c2=a2*b2
c1,c2= simplify(c1,c2)
# print the result of subtraction
print("subtraction: " + str(c1)+ "/" +str(c2) )

#multiplication
c1=a1*b1
c2=a2*b2
c1,c2= simplify(c1,c2)
# print the result of multiplication
print("multiplication: "+ str(c1)+ "/" +str(c2) )

#divide
c1=a1*b2
c2=a2*b1
c1,c2= simplify(c1,c2)
# print the result of division
print("division: "+ str(c1)+ "/" +str(c2) )
