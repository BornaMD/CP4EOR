class Person():
  def __init__(self,s_name,kg_weight,m_height):
    self.name=s_name
    self.weight=kg_weight
    self.height=round(m_height, 1)

  def getBMI(self):     #weight/(height**2)
    bmi=self.weight/(self.height**2)
    return bmi

  def isHealthy(self):
    bmi=self.getBMI()
    if bmi>18.5 and bmi<25:
      return True
    return False

#  def __str__(self):
#    return "{0} ({1}kg, {2}m)".format(self.name,self.weight, self.height)


