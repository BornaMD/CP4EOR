n=int(input("How many numbers do you have? "))
a=[None]*n
sum=0
for i in range(0,n):
    a[i]=int(input("Give a number: "))
    sum+=a[i]
print(sum/n)

a=[[0,0,0],[0,0,0]]
b=[[0,0],[0,0],[0,0]]
c=[[0,0],[0,0]]

#get the matrices a and b from user 
for j in range(0,2):
    for i in range(0,3):
        a[j][i]=int(input("Give element a"+str(j)+""+str(i)+" of matrix A: "))
for j in range(0,3):
    for i in range(0,2):
        b[j][i]=int(input("Give element b"+str(j)+""+str(i)+" of matrix B: "))

#calculate the multiplication result
for i in range(0,3):
    c[0][0]+= a[0][i]*b[i][0] 
for i in range(0,3):
    c[0][1]+= a[0][i]*b[i][1] 

for i in range(0,3):
    c[1][0]+= a[1][i]*b[i][0] 
for i in range(0,3):
    c[1][1]+= a[1][i]*b[i][1] 

print(c[0][0],",",c[0][1])
print(c[1][0],",",c[1][1])