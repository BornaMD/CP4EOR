int x=5
x=5
y=5
x=y
x="book"

x = 1   
y = 2.8 
z = 1j  

print(type(x))
print(type(y))
print(type(z))  

b = "Hello, World!"
print(b[2:5]) 


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) 

thislist = ["apple", "banana", "cherry"]
thislist[0] = "banana"
print(thislist) 

thistuple = ("apple", "banana", "cherry")
thistuple[0] = "banana"
print(thistuple) 		

thisset = {"apple", "banana", "cherry"}
thisset[0] = "banana"
print(thisset)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict[0] = "banana"
print(thisdict)

thistuple = ("apple", "banana", "cherry")
thistuple[1] = "blackcurrant" 
print(thistuple)


a = 20
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b") 

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 