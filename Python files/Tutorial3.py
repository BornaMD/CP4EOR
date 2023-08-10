#13
def count_by_case(string):
     upper = sum(letter.isupper() for letter in string)
     lower = len(string) - upper
     return lower, upper
while True:
    try: 
      string=str(input("Count the upper- lowercase ratio for:"))
    lower, upper = count_by_case(string)
 print("{!r} contains {} upper and {} lower case letters".format(string, upper, lower))

#14
import re
p= input("Input your password:")
x = True
while x:
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print(p)
        x=False
        break

if x:
    print("Not a Valid Password")

#14
#imports and variable definitions
import re

#inputs and pre-processing
print("Please enter multiple passwords separated using commas.")
p= input("Input your password:")
#opdelen in hapbare porties
#make list l from splitting p
l = []
#processing
x = True
p=l(i)
while x:
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print(p)
        x=False
        break

#returns and output
if x:
    print("Not a Valid Password")