#Dutch:
class Customer:
    Revenue=0
    def __init__(self,custID):
        fh=open("Customers.txt","r")
        custLines=fh.readlines()
        fh.close()
        LineNumber=0
        for c in custLines:
            custParts=c.strip().split("|")
            if custParts[0]==custID:
                self.__custID=custParts[0]
                self.__PaidUs=custParts[1]
                Customer.Revenue+=int(custParts[1])
                self.__custName=custParts[2]
                self.__LineNumber=LineNumber 
            LineNumber+=1
        self.__custLines=custLines
    
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
        Customer.Revenue+=int(self.__PaidUs)
        self.__PaidUs = PaidUs
        self.__save()
        
    def AddToPaidUs(self, amount):
        self.PaidUs= str(int(self.PaidUs) + amount)

    def getNameWithSuffix(self,Inc):
        if Inc==True:
            return self.custName + " Inc."
        else:
            return self.custName + " Ltd."

    #added to support i=c1+c2 in the __main__
    def __add__(self, cust):
        return int(self.PaidUs) + int(cust.PaidUs)

#American
c1=Customer("2")
c2=Customer("3")
i=c1+c2 
print("Customers 2 and 3 paid us ",i)

# Excercise 7

#Dutch:
class Customer:
    Revenue=0
    @classmethod
    def getPaidTax(cls):
        return cls.Revenue*0.21
    
    def __init__(self,custID):
        fh=open("Customers.txt","r")
        custLines=fh.readlines()
        fh.close()
        LineNumber=0
        for c in custLines:
            custParts=c.strip().split("|")
            if custParts[0]==custID:
                self.__custID=custParts[0]
                self.__PaidUs=custParts[1]
                Customer.Revenue+=int(custParts[1])
                self.__custName=custParts[2]
                self.__LineNumber=LineNumber 
            LineNumber+=1
        self.__custLines=custLines
    
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
        Customer.Revenue+=int(self.__PaidUs)
        self.__PaidUs = PaidUs
        self.__save()
        
    def AddToPaidUs(self, amount):
        self.PaidUs= str(int(self.PaidUs) + amount)

    def getNameWithSuffix(self,Inc):
        if Inc==True:
            return self.custName + " Inc."
        else:
            return self.custName + " Ltd."

    #added to support i=c1+c2 in the __main__
    def __add__(self, cust):
        return int(self.PaidUs) + int(cust.PaidUs)

#American
c1=Customer("2")
c2=Customer("3")
i=c1+c2 
print("Customers 2 and 3 paid us ",i)

