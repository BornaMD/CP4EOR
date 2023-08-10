class clsFraction:
  
  def __init__(self, Numerator=0, Denominator=1):
    if Denominator==0:
      raise Exception("Denominator cannot be zero")
    self.__N=Numerator
    self.__D=Denominator
  
  def setD(self, Denominator=1):
    if Denominator==0:
      raise Exception("Denominator cannot be zero")
    self.__D=Denominator
  
  def getD(self):
    self.__simplify()
    return self.__D

  def setN(self, Numerator=0):
    self.__N=Numerator
  
  def getN(self):
    self.__simplify()
    return self.__N
  
  def __simplify(self):
    import math as m
    g=m.gcd(self.numerator,self.denominaor)
    self.numerator //=g
    self.denominaor //=g

def __str__(self):
    self.__simplify()
    if(self.__D==1):
      return str(self.__N)
    #return str(self.__N) + "/" + str(self.__D)
    return "{0}/{1}".format(self.__N, self.__D)

