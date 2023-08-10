print(3/0)
		

print(k)

#k is not created in the RAM before being printed
		

#None of the above

s=""

for i in range(1,13):

     s= s + (i*4)

print (s)

s=""

for i in range(1,13):

     s= s + (i*4)

print (s)


		

print(3+"3")
		

print(3/0)
		

print(k)

for j in range(1,13):
 s=""
 for i in range (1,13):
   s+= str(i*j) + " " * (1+3-len(str(i*j)))
 print (s)

for j in range(1,13):
 s=""
 for i in range (1,13):
  k=str(i*j)
  s+= k + " " * (1+3-len(k))
 print (s)

m=int(input("Develop multiplication table for:"))
MaxSize= len(str(m*m))

for j in range(1,m+1):
 s=""
 for i in range (1,m+1):
  k=str(i*j)
  s+= k + " " * (1+MaxSize-len(k))
print (s)

try:
 m=int(input("Develop multiplication table for:"))
except Exception:
 print("Oops!That was no valid number. Please try again.")
 m=int(input("Develop multiplication table for:"))
MaxSize= len(str(m*m))
for j in range(1,m+1):
 s=""
 for i in range (1,m+1):
  k=str(i*j)
  s+= k + " " * (1+MaxSize-len(k))
print (s)




