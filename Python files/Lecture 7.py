# Exercise 0

import mdlFraction as frc 

def add3fractions(a, parameter_list):
  pass
  
print("sum: " + str(e1) + "/" + str(e2))


# Properties validate the data and store it in the attribute.
# Using 2 underscores make a method or an attribute private.
# Private attibute: __D; private method: __gdc
# Something that is made private is not accessible to the user of a definition, only someone who has access to the definition file itself can access the private attibutes, functions and methods.

class Point:
  """ Point class represents and manipulates x,y coords. """
  
  def __init__(self, x=0, y=0):
    """ Create a new point at x, y """
    self.x = x
    self.y = y

class clsFraction:
  """ A class that represents a fraction""" 


# self can be defined by everything when calling the definition, meaning that the definition can be used in all forms.
# When calling __defName(self); 
# Use 
 
# Exericise 1

fh=open("C:\\Users\\Gebruiker\\Google Drive\\Python 2018\\Lecture Slides\\07-File\\codes\\Customers.txt","r+")
L=fh.readline()

class Customer:
  """Stores the customer's data"""

  def __init__(self, custID):
    self.custID = custID 
    L = fh.readline()
    CustID = L[0]
    PaidUS = L[1]
    custName = L[2]

    for i in L:
      if custID == L[i]:
        return 
        break
      else:
        break

class Customer:
  
  def __init__(self,custID):
    fh=open("Customers.txt", "r")
    custLines=fh.readlines()
    for c in custLines:
      custParts=c.strip().split("|")
      if custParts[0]==custID:
        self.custID=custParts[0]
        self.PaidUS=custParts[1]
        self.custName=custParts[2]

c=Customer("5")
print("Customer (",c.custID,") name=",c.custName," paid us= ",c.PaidUS)

# Exercise 2

class Customer:
  
  def __init__(self,custID):
    fh=open("Customers.txt", "r")
    custLines=fh.readlines()
    for c in custLines:
      custParts=c.strip().split("|")
      if custParts[0]==custID:
        self.__custID=custParts[0]
        self.__PaidUS=custParts[1]
        self.__custName=custParts[2]

c=Customer("5")
print("Customer (",c.custID,") name=",c.custName," paid us= ",c.PaidUS)

