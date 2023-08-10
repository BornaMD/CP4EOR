#i=2
#print(type(i))
#print(id(i))
#print(i)~

##

#  k=i+3
#  print(k)
#  j=i.__add__(3)
#  print(j.__str__())

class Point:
  """ Create a new Point, at coordinates x, y """

  def __init__(self, x_=0, y_=0):
    """ Create a new point at x, y """
    self.x = x_
    self.y = y_