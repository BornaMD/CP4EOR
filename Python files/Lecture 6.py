# Exercises
# 0
#matrix_length = int(input("Put in the rows of the matrix: "))
#matrix_ = int(input("Put in the rows of the matrix: "))

#for i in range(1, matrix_length):
#    row[i] = list(input("Put in row" + str(i) +"of the matrix: "))

#ans
matrix=[]
L=input("Give the fist line of the matrix: ")
while L.strip()!="":
  matrix.append([int(s) for s in L.split()]) 
  L=input("Give the next row of the list, [enter nothing if you are done]: ")

print("matrix=", matrix)

#06-01
fh=open("C:\\Users\\Gebruiker\\Google Drive\\Python 2018\\Lecture Slides\\06-File\\codes\\fractions-1.txt","r")
s=fh.read()

print("s=\n",s)
print("s[0]=",s[0])
print("s[1]=",s[1])
print("s[2]=",s[2])
print("s[3]=",s[3])
print("s[4]=",s[4])
print("s[5]=",s[5])
print("s[6]=",s[6])

print(r"Is s[3] equal to \n?",s[3]=="\n")
fh.close()

#06-02
fh=open("C:\\Users\\Gebruiker\\Google Drive\\Python 2018\\Lecture Slides\\06-File\\codes\\fractions-1.txt","r")
L=fh.readlines()

print("L[0]=",L[0])  #3 4\n
print("L[1]=",L[1])  #1 8EOF
print("L[0][0]=",L[0][0])
print("L[0][1]=",L[0][1])
print("L[0][2]=",L[0][2])
print("L[0][3]=",L[0][3])
print("L[1][0]=",L[1][0])
print("L[1][1]=",L[1][1])
print("L[1][2]=",L[1][2])
fh.close()

#06-02(v2)
fh=open("C:\\Users\\Gebruiker\\Google Drive\\Python 2018\\Lecture Slides\\06-File\\codes\\fractions-1.txt","r")
numerator=[]
denominator=[]
entireFileinRAM=fh.readlines()
for L in entireFileinRAM:
    #L is like "3 4\n"
    if (L.rstrip()!=""): #if L is not blank space
        numerator.append(int(L[0]))
        denominator.append(int(L[2]))
fh.close()
print("numerators= ",numerator)
print("denominators= ", denominator)
print("first fraction= ",numerator[0], "/", denominator[0])
print("second fraction= ",numerator[1], "/", denominator[1])

#06-03
fh=open("C:\\Users\\Gebruiker\\Google Drive\\Python 2018\\Lecture Slides\\06-File\\codes\\fractions-1.txt","r")

i=0
L=fh.readline()
while L!="":
    print(i," : ", L)
    i+=1
    L=fh.readline()
    
fh.close()

#06-04
fh=open("C:\\Users\\Gebruiker\\Google Drive\\Python 2018\\Lecture Slides\\06-File\\codes\\fractions-1.txt","r")
numerator=[]
denominator=[]
L=fh.readline()
while L!="":
    numerator.append(int(L[0]))
    denominator.append(int(L[2]))
    L=fh.readline()
fh.close()
print("numerators= ",numerator)
print("denominators= ", denominator)
print("first fraction= ",numerator[0], "/", denominator[0])
print("second fraction= ",numerator[1], "/", denominator[1])

# Exercise 1
fh=open("C:\\Users\\Gebruiker\\Google Drive\\Python 2018\\Lecture Slides\\06-File\\codes\\matrix-1.txt","r")

matrix=[]
L=fh.readline()
while L!="":
  matrix.append([int(s) for s in L.split()]) 
  L=fh.readline()
fh.close()
print("matrix=\n\r", matrix)

# Example of writing a file

import mdlFraction
#read the fractions
fh=open("fractions-2.txt","r")
numerator=[]
denominator=[]
L=fh.readline()
while L!="":
  numerator.append(int(L[0]))
  denominator.append(int(L[2]))
  L=fh.readline()
fh.close()    

#calculate the sum of two fractions
c1=numerator[0]*denominator[1]+numerator[1]*denominator[0]
c2=denominator[0]*denominator[1]
c1,c2=mdlFraction.simplify(c1,c2)
#write the result at the end of the file
fh=open("fractions-2.txt","a")
fh.write("\n"+str(c1)+" "+str(c2))

fh.close()

fh=open("fractions-4.txt","r")
content=fh.read()
fh.close()
fh=open("fractions-4-backup.txt","w")
fh.write(content)
fh.close()

# Edit a file (06-13)

old=input("Enter the old value: ") #3 4
new=input("Enter the new value: ") #5 7
newContent=""
fh=open("fractions-4.txt","r")
oldContent=fh.readlines()

for L in oldContent:
    #L is like "3 4\n" or "13 4"
    if (L.rstrip()==old):
        newContent+=new+"\n"
    else:
        newContent+=L

fh.close()
fh=open("fractions-4.txt","w")
fh.write(newContent)
fh.close()

M=[[3, 4, 7], 
  [1, 8, 10],
  [4, 5, 6],
  [9, 0, 2]]
L=[]
for i in range(len(M)):
  if M[i][0] !="":
    L[i].append([int(M[i][s]) for s in M.split()])
    fh=open("matrix-1.txt","w")
    L=fh.write(L)
fh.close()

# actual answer
matrix=[]
L=input("Give the fist line of the matrix: ")
while L.rstrip()!="":
  matrix.append([int(s) for s in L.split()]) 
  L=input("Give the next row of the list, [enter nothing if you are done]: ")
print("given matrix is: ", matrix)

with open("matrix-1.txt", "w") as fh:
  for r in matrix:
    for c in r:
      fh.write(str(c) + " ")
    fh.write("\n")

fh.close()

# Exercies 3 (4 actually)
fh=open("fractions-5.txt","r")
oldContent=fh.readlines()
result = 0
for i in range(len(oldContent)):
  if oldContent[i][0] != "":
    result == oldContent

# Answer
import mdlFraction as frc 

fh=open("fractions-5.txt", "r")

L=fh.readline().strip().split()
a1=int(L[0])
a2=int(L[1])

while(len(L)>0):
  L=fh.readline().strip().split()

  if(len(L)==0):
    break
  opr=L[0]
  L=fh.readline().strip().split()
  b1=int(L[0])
  b2=int(L[1])

  if(opr=="+"):
    c1=a1*b2+a2*b1
    c2=a2*b2
    c1,c2 =frc.simplify(c1,c2)

  elif(opr=="-"):
    c1=a1*b2-a2*b1
    c2=a2*b2
    c1,c2 =frc.simplify(c1,c2)

  elif(opr=="*"):
    c1=a1*b1
    c2=a2*b2
    c1,c2 =frc.simplify(c1,c2)

  elif(opr=="/"):
    c1=a1*b2
    c2=a2*b1
    c1,c2=frc.simplify(c1,c2)

  else:
    pass

  a1=c1
  a2=c2

print(a1, "/", a2)

