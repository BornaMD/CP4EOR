# Exercise 0

import mdlFraction as frc 

def add3fractions(a1=0, a2=1, b1=0, b2=1, c1=0, c2=1):
  d1=a1*b2+a2*b1
  d2=a2*b2
  d1,d2= frc.simplify(d1,d2)
  
  e1=c1*d2+c2*d1
  e2=c2*d2
  e1,e2=frc.simplify(e1,e2)
  return e1,e2

a1=1
a2=5
b1=2
b2=7
c1=4
c2=9
e1,e2=add3fractions()
print("Sum of fractions: " + str(e1) + "/" + str(e2))

# Exericise 1

class Customer:
  
  def __init__(self,custID):
    fh=open("Customers.txt", "r")
    daad=fh.readlines()
    for c in daad:
      custParts=c.strip().split("|")
      if custParts[0]==custID:
        self.custID=custParts[0]
        self.PaidUs=custParts[1]
        self.custName=custParts[2]

c=Customer("5")
print("Customer (",c.custID,") name=",c.custName," paid us= ",c.PaidUs)

# Exercise 2

class Customer:
  
  def __init__(self,custID):
    fh=open("Customers.txt", "r")
    daad=fh.readlines()
    LineNumber=0
    for c in daad:
      custParts=c.strip().split("|")
      if custParts[0]==custID:
        self.__custID=custParts[0]
        self.__PaidUs=custParts[1]
        self.__custName=custParts[2]
        self.__LineNumber=LineNumber
      LineNumber+=1
    self.__custLiness=daad
  
  def __save(self):
    self.__custLines[self.__LineNumnber]=self.__custID+"|"+self.__PaidUs+"|"+self.__custName+"\n"
    fh=open("customers.txt", "w")
    for l in self.__custLines:
      fh.write(l)
    fh.close()  

  @property
  def custID(self):
    return self.__custID
  @custID.setter
  def custID(self, custID):
    self.__custID = custID
    self.__save()

  @property
  def custName(self):
    return self.__custName
  @custName.setter
  def custName(self, custName):
    self.__custName = custName
    self.__save()
      
@property
  def PaidUs(self):
    return self.__PaidUs
  @PaidUs.setter
  def PaidUs(self, PaidUs):
    self.__PaidUs = PaidUs
    self.__save()


c=Customer("5")
c.custName=ÏNDD
print("Customer (",c.custID,") name=",c.custName," paid us= ",c.PaidUs)

