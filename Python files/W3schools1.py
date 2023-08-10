if 5 > 2:
  print("Five is greater than two!")
#This is a comment.
print("Hello, World!")
"""This is a
multiline docstring."""
print("Hello, World!")
x = 5
y = "John"
print(x)
print(y)
x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)
x = "awesome"
print("Python is " + x)
x = "Python is "
y = "awesome"
z =  x + y
print(z)
x = 5
y = 10
print(x + y)

x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z)) 
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z)) 
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z)) 
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z)) 
print(x)
print(y)
print(z) 

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0' 
a = "Hello, World!"
print(a[1])
b = "Hello, World!"
print(b[2:5])
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
a = "Hello, World!"
print(len(a))
a = "Hello, World!"
print(a.lower())
a = "Hello, World!"
print(a.upper())
a = "Hello, World!"
print(a.replace("H", "J"))
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 



thistuple = ("apple", "banana", "cherry")
print(thistuple)
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))
thisset = {"apple", "banana", "cherry"}
print(thisset) 
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) 
thisset = set(("apple", "banana", "cherry"))
thisset.add("damson")
print(thisset) 
thisset = set(("apple", "banana", "cherry"))
thisset.remove("banana")
print(thisset) 
thisset = set(("apple", "banana", "cherry"))
print(len(thisset))

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
x = thisdict["model"]
x = thisdict.get("model")
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

for x in thisdict:
  print(x) 
for x in thisdict:
  print(thisdict[x])
for x in thisdict.values():
  print(x) 
for x, y in thisdict.items():
  print(x, y) 
print(len(thisdict)) 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict) 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict) 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict) 
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
if a > b: print("a is greater than b")
print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B") 
if a > b and c > a:
  print("Both conditions are True")
if a > b or a > c:
  print("At least one of the conditions are True")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 

# Sets
thisset = {"word", "red", "ter", "komans"}
theset = {"word", "red", "soon", "komas", "inter"}
x = theset.difference_update(thisset)
y = theset.intersection_update(thisset)
print(theset.difference(thisset))
print(x)
# Ask why it prints 'None'
print(y)
