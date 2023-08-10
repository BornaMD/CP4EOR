#both American and Dutch in one file
# Look for "stage 2" to learn how I used classmethods to print all created functions and calculate their sum 
class clsFraction:
  ''' A class that represents a fraction.
      Attributes:
        Numerator: the top number in the fraction.
        Denominator: the bottom number in the raction.
  '''

  # stage 2: class attribute: Keeps all created fraction to be used
  AllFractions=[]
  
  def __init__(self, Numerator=0, Denominator=1):
    ''' Initializes clsFraction with two numbers for Numerator and Denominator '''
    self.__N=Numerator
    self.__D=Denominator
    self.__simplify()
    # stage 2: the new fraction is added to the list
    clsFraction.AllFractions.append(self)

  # stage 2: This classmethod prints all created fractions  
  @classmethod
  def PrintAll(cls):
    i=0
    for r in clsFraction.AllFractions:
        print("Fraction[%s]: %s"  % (i,r))
        i+=1

  # stage 2: This classmethod calculates the sum of all fractions
  @classmethod
  def SumOfAll(cls):
      R=clsFraction()
      for f in clsFraction.AllFractions:
        if(f!=R):
            R.AddToMe(f)
      #clsFraction.AllFractions.remove(R)
      return R  

  # stage 2: write this classmethod yourself that calculates the average of all fractions
  @classmethod
  def AverageOfAll(cls):
      return "None" 


  #customizing print
  def __str__(self):
     if(self.D==1):
       return str(self.N)
     return str(self.N) + "/" + str(self.D)

  #private functions
  def __gcd(self, x,y):
      while y != 0:
          (x, y) = (y, x % y)
      return x

  def __simplify(self):
      g=self.__gcd(self.__N,self.__D)
      self.__N //= g
      self.__D //= g
  
  #properties
  @property
  def N(self):
        return self.__N
  
  @N.setter
  def N(self, Numerator):
        self.__N = Numerator
        self.__simplify()
  
  @property
  def D(self):
        return self.__D
  
  @D.setter
  def D(self, Denominator):
        if Denominator==0: raise Exception("Denominator cannot be zero")
        self.__D = Denominator
        self.__simplify()
  
  #public methods
  def AddToMe(self, another_fraction):
    self.N= self.N * another_fraction.D +self.D * another_fraction.N
    self.D= self.D * another_fraction.D
  
  def Add(self,another_fraction):
    R=clsFraction()
    R.AddToMe(self)
    R.AddToMe(another_fraction)
    return R

  def __add__(self, another_fraction):
      R=clsFraction()
      R.AddToMe(self)
      R.AddToMe(another_fraction)
      return R

  def __mul__(self, another_fraction):
      R=clsFraction()
      R.N=self.N*another_fraction.N
      R.D=self.D*another_fraction.D
      return R


#----American----

f1=clsFraction(3,8)
f2=clsFraction(4,3)

f3=f1*f2*f1*f2

print(f1)
print(f2)
print(f3)

# stage 2: how the American uses the classmethods
print(clsFraction.AllFractions[0])
clsFraction.PrintAll() #stage 2: you see that f3=f1*f2*f1*f2 in the above creates an instance for each *
print(clsFraction.SumOfAll()) #stage 2: Note that SumOfAll creates a new instance of clsFraction to keep the sum
