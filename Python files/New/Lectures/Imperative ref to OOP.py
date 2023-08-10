##point is the name of the file (point.py)
##Point is the name of the class in that file
from point import Point
#x1=int(input("Enter x1: "))
#y1=int(input("Enter y1: "))
#x2=int(input("Enter x2: "))
#y2=int(input("Enter y2: "))
##creating instances of the class Point
#point1=Point(x1,y1)
#point2=Point(x2,y2)
#point3=Point() #(0,0) origin
#
##...
##setting attributes to new values
#point3.x=int(input("Enter x3: "))
#point3.y=int(input("Enter y3: "))
##retrieving the value of an attribute
#i=point1.x
#j=point1.y
#print("Point 1 is (%d,%d)"%(i,j))
#print("Point 2 is ({},{})".format(point2.x,point2.y))
#print("Point 3 is ({0},{1})".format(point3.x,point3.y))

##

#from Person import Person
#
#aname = input(" Please provide the name of person 1: ")
#aweight = int(input(" Please provide the weight in KG of person 1: "))
#aheight = float(input(" Please provide the height in M.xx of person 1: "))
#
#bname = input(" Please provide the name of person 2: ")
#bweight = int(input(" Please provide the weight in KG of person 2: "))
#bheight = float(input(" Please provide the height in M.xx of person 2: "))
#
#p1=Person(aname,aweight,aheight )
#p2=Person(bname,bweight,bheight )
#
#print(p1, "\n", p2)

##

#from student import Student
#s1=Student("Brad Pitt",20190112,[8,9,4,5])
#s1.name="William Bradley Pitt"
#s1.sid=20190113
#s1.GPAperYears=[8.5,9,4,5,7.5]
#print(s1)

#using an instance method
#point4=Point(3,4)
#point5=Point(5,6)
#d4=point4.distance_from_origin() #returns 5.0
#d5=point5.distance_from_origin() #returns 7.8
#
#print(d4, " \n", round(d5, 2))

##

from Person import Person
#
#aname =  "Dana"   #input(" Please provide the name of person 1: ")
#aweight = 57    #int(input(" Please provide the weight in KG of person 1: "))
#aheight = 1.65    #float(input(" Please provide the height in M.xx of person 1: "))
#
#bname = "Borna"    #input(" Please provide the name of person 2: ")
#bweight = 59    #int(input(" Please provide the weight in KG of person 2: "))
#bheight = 1.69    #float(input(" Please provide the height in M.xx of person 2: "))
#
#p1=Person(aname,aweight,aheight )
#p2=Person(bname,bweight,bheight )
#
#b1 = p1.getBMI()
#b2 = p2.getBMI()
#
#print(b1, "\n", b2)

#p1=Person("Amin",90,1.80)
#print(p1)

#from SimpleFraction import SimpleFraction
##F1=SimpleFraction(1,5)
##F2=SimpleFraction(3,5)
##F3=F1+F2 #(20/25)
##print(F3)
#
#F1=SimpleFraction(1,5)
#F2=SimpleFraction(3,5)
#F3=F1+F2 #(20/25)
#print(F3)


from mdlFraction import simplify
a1=1 #=int(input("Give a nominator:"))
a2=5 #=int(input("Give a denominator:"))
b1=2 #=int(input("Give a nominator:")
b2=7 #=int(input("Give a denominator:"))
c1=4 #=int(input("Give a nominator:")
c2=9 #=int(input("Give a denominator:"))

#add a and b and put the result in d
d1=a1*b2+a2*b1
d2=a2*b2
d1,d2= simplify(d1,d2)
#add d and c and put the result in e
e1=c1*d2+c2*d1
e2=c2*d2
e1,e2= simplify(e1,e2)
# print the result of summation
print("sum: " + str(e1)+ "/" +str(e2) )

from SimpleFraction import SimpleFraction
a1=1 #=int(input("Give a nominator:"))
a2=5 #=int(input("Give a denominator:"))
b1=2 #=int(input("Give a nominator:")
b2=7 #=int(input("Give a denominator:"))
c1=4 #=int(input("Give a nominator:")
c2=9 #=int(input("Give a denominator:"))

A=SimpleFraction(a1,a2)
B=SimpleFraction(b1,b2)
C=SimpleFraction(c1,c2)
E=A+B+C
print("sum: " + str(E))



