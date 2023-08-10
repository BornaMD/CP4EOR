hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50
areas=[hall, kit, liv, bed, bath]
print(areas)
areas=hall + kit + liv + bed + bath
print(areas)		
areas=[hall] + [kit] + [liv] + [bed] + [bath]
print(areas)		
areas=[hall], [kit], [liv], [bed], [bath]
print(areas)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]
print(areas)
print([1 + 2, "a" * 5, 3])
print([[1, 2, 3], [4, 5, 7]])
print([1, 3, 4, 2])
print([2 * 6, 3 * 2, 3 * 2])
A=[11,32,30,14,5,6]
A[-len(A)]
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
print( 		

areas[len(areas)//2-2])
A= [11, 12, 13, 14, 11, 12, 13]
print(A[:3])
print(A[4:])
print(A[-7:-4])
print(A[5:7])
x = [["a", "b", "c"],

     ["d", "e", "f"],

     ["g", "h", "i"]]
print( 		

x[2][1])

x= ["a","b","c"]
print(x)
x[0]="d"
print(x)
y=x[:]
y[0]="d"
print(x)
y=x
y[0]="d"
print(x)

x=[1,2,3]

y= x+ [4,5]

y[0]=-7

print(x)
print(y)
areas = ["hallway", 11.25, "kitchen", 18.0,         "chill zone", 20.0, "bedroom", 10.75,          "bathroom", 10.50, "poolhouse", 24.5,          "garage", 15.45]
print(areas)
del(areas[10:11])
print(areas)
import numpy as np
h = [1.73,1.68,1.79] 
np_h=np.array(h) 
print(np_h[ np_h<1.7 ])
print(np_h[0,1])