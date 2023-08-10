#Properties are used to check the value that wants to be assigned to the private attribute.

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

# Exercise 3
#Dutch:
class Customer:
  def __init__(self,custID):
    fh=open("Customers.txt","r")
    custLines=fh.readlines()
    fh.close()
    LineNumber=0 #added for the sake of saving
    for c in custLines:
      custParts=c.strip().split("|")
      if custParts[0]==custID:
        self.__custID=custParts[0]
        self.__PaidUs=custParts[1]
        self.__custName=custParts[2]
        self.__LineNumber=LineNumber #added for the sake of saving
      LineNumber+=1 #added for the sake of saving
    self.__custLines=custLines #added for the sake of saving
    
  def __save(self):
      self.__custLines[self.__LineNumber]=self.__custID+"|"+self.__PaidUs+"|"+self.__custName+"\n"
      fh=open("Customers.txt","w")
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
  def custName(self, name):
      self.__custName = name
      self.__save()

  @property
  def PaidUs(self):
      return self.__PaidUs
  @PaidUs.setter
  def PaidUs(self, PaidUs):
      self.__PaidUs = PaidUs
      self.__save()

#American
c=Customer("5")
c.custName="INDD"  
print("Customer (",c.custID,") name=",c.custName," paid us= ",c.PaidUs)

# Exercise 4
#Dutch:
class Customer:
    def __init__(self,custID):
        fh=open("Customers.txt","r")
        custLines=fh.readlines()
        fh.close()
        LineNumber=0 #added for the sake of saving
        for c in custLines:
            custParts=c.strip().split("|")
            if custParts[0]==custID:
                self.__custID=custParts[0]
                self.__PaidUs=custParts[1]
                self.__custName=custParts[2]
                self.__LineNumber=LineNumber #added for the sake of saving
            LineNumber+=1 #added for the sake of saving
        self.__custLines=custLines #added for the sake of saving
    
    def __save(self):
        self.__custLines[self.__LineNumber]=self.__custID+"|"+self.__PaidUs+"|"+self.__custName+"\n"
        fh=open("Customers.txt","w")
        for l in self.__custLines:
            fh.write(l)
        fh.close()

    def AddToPaidUs(self, amount):
      self.PaidUs = str(int(self.PaidUs) + amount)
      
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
    def custName(self, name):
        self.__custName = name
        self.__save()

    @property
    def PaidUs(self):
        return self.__PaidUs
    @PaidUs.setter
    def PaidUs(self, PaidUs):
        self.__PaidUs = PaidUs
        self.__save()

#American
c=Customer("4")
c.AddToPaidUs(200)  
print("Customer (",c.custID,") name=",c.custName," paid us= ",c.PaidUs)

# Exercise 5
#Dutch:
class Customer:
  def __init__(self,custID):
    fh=open("Customers.txt","r")
    custLines=fh.readlines()
    fh.close()
    LineNumber=0 #added for the sake of saving
    for c in custLines:
      custParts=c.strip().split("|")
      if custParts[0]==custID:
          self.__custID=custParts[0]
          self.__PaidUs=custParts[1]
          self.__custName=custParts[2]
          self.__LineNumber=LineNumber #added for the sake of saving
      LineNumber+=1 #added for the sake of saving
    self.__custLines=custLines #added for the sake of saving
  
  def __save(self):
    self.__custLines[self.__LineNumber]=self.__custID+"|"+self.__PaidUs+"|"+self.__custName+"\n"
    fh=open("Customers.txt","w")
    for l in self.__custLines:
        fh.write(l)
    fh.close()

  def AddToPaidUs(self, amount):
    self.PaidUs = str(int(self.PaidUs) + amount)
    
  def getNameWithSuffix(self, suffix):
    if suffix == True:
      return self.custName + " Inc."
    elif suffix == False:
      return self.custName + " Ltd."

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
  def custName(self, name):
    self.__custName = name
    self.__save()

  @property
  def PaidUs(self):
    return self.__PaidUs

  @PaidUs.setter
  def PaidUs(self, PaidUs):
    self.__PaidUs = PaidUs
    self.__save()

#American
c=Customer("4")
c.AddToPaidUs(200)  
print("Customer (",c.custID,") name=",c.custName," paid us= ",c.PaidUs)

# Exercise 5
#Dutch:
class Customer:
  def __init__(self,custID):
    fh=open("Customers.txt","r")
    custLines=fh.readlines()
    fh.close()
    LineNumber=0 #added for the sake of saving
    for c in custLines:
      custParts=c.strip().split("|")
      if custParts[0]==custID:
          self.__custID=custParts[0]
          self.__PaidUs=custParts[1]
          self.__custName=custParts[2]
          self.__LineNumber=LineNumber #added for the sake of saving
      LineNumber+=1 #added for the sake of saving
    self.__custLines=custLines #added for the sake of saving
  
  def __save(self):
    self.__custLines[self.__LineNumber]=self.__custID+"|"+self.__PaidUs+"|"+self.__custName+"\n"
    fh=open("Customers.txt","w")
    for l in self.__custLines:
        fh.write(l)
    fh.close()

  def AddToPaidUs(self, amount):
    self.PaidUs = str(int(self.PaidUs) + amount)
    
  def getNameWithSuffix(self, suffix):
    if suffix == True:
      return self.custName + " Inc."
    elif suffix == False:
      return self.custName + " Ltd."

  def __add__(self, OCust):
    return int(self.PaidUs) + int(OCust.PaidUs)
  
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
  def custName(self, name):
    self.__custName = name
    self.__save()

  @property
  def PaidUs(self):
    return self.__PaidUs

  @PaidUs.setter
  def PaidUs(self, PaidUs):
    self.__PaidUs = PaidUs
    self.__save()

#American
c1=Customer("2")
c2=Customer("3")
i=c1+c2
print("Customers 2 and 3 paid us ",i)

# Lecture 9
# __simplify does change the state of the class and reads the state of the class.
# __gcd does not change the state of the class and does not read the state of the class.
# __str__ does not change the state of the class and does read the state of the class 
# Add and __add__ does not change the state of the class and does read the state of the class.
# AddToMe does change the state of the class and does read the state of the class.
# This can be found by looking at if the self or any of the other variables THAT ARE PART of the class change in its assigned value. 

# Exercise 8 Answer:
class clsFraction:
  #...
  @staticmethod
  def Add(F1, F2):
    #option 1
    return F1 + F2

    #option 2
    R=clsFraction()
    R.N=F1.N * F2.D + F2.N * F1.D 

#The @staticmethod can be used in other classes and adjusted in the main. (adjusting it in the main is not preffered, but possible). 

# Exercise 9:

class UniEmployee:
  def __init__(self, firstname, lastname, fte, degree):
    self.firstname=firstname
    self.lastname=lastname
    self.fte=fte
    self.degree=degree

  def __str__(self):
    return "{0},{1},{2},{3}".format(self.firstname,self.lastname, self.fte,self.degree)

  def AppendToFile(slef,filename):
    with open(filename, "a") as fh:
      fh.write(self.__str__()+"\n")

# Exercise 10:

class UniEmployee:
  def __init__(self, firstname, lastname, fte, degree, papers, courses):
    self.firstname=firstname
    self.lastname=lastname
    self.fte=fte
    self.degree=degree
    self.papers=papers
    self.couses=courses

  def __str__(self):
    return "{0},{1},{2},{3},{4},{5}".format(self.firstname,self.lastname, self.fte,self.degree,self.papers,self.courses)

  def AppendToFile(slef,filename):
    with open(filename, "a") as fh:
      fh.write(self.__str__()+"\n")

# In OOP-diagrams an arrow is used to indicate inheritance.

# Exercise 11:
class Secretary(UniEmployee):
  def __init__(self,firstname, lastname,fte,degree,skills,responsibilities):
    UniEmployee.__init__(self,firstname, lastname,fte,degree) 
    self.skills=skills
    self.responsibilities=responsibilities
  def __str__(self):
    s=UniEmployee.__str__(self) #using the __str__ method of parent
    return
    s+",{0},{1}".format(self.skills,self.responsibilities)

