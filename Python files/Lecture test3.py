a = []
for i in range (0,5):
    a.append(i)
a.insert(0,2)  
a.pop(1) 
print(a)

a=[None]*6
sum=0

for i in range(0,6):
    a[i]=int(input("Give a number: "))


for i in range(0,6):
    sum+=a[i]

print(sum/6)

'''
sum=
 a[0]
+a[1]
+a[2]
+a[3]
+a[4]