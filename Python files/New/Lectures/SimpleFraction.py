import math as m

class SimpleFraction:
  def __init__(self,N=0,D=1):
    self.nominator=N
    self.denominator=D

  def __str__(self):
    return "{0}/{1}".format(self.nominator,self.denominator)

  def __add__(self, other):
    f=SimpleFraction(0,1)
    f.nominator=self.nominator*other.denominator + self.denominator*other.nominator
    f.demoninator=self.denominator * other.denominator
    f.simplify()
    return f
  def simplify(self):
    x=m.gcd(self.nominator, self.denominator)
    self.nominator //= x
    self.denominator //= x

#  def __gcd__(self):
#    f.nominator=m.gcd(f.nominator,f.denominator)
#    return f


