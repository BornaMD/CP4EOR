class Point:
  """ Create a new Point, at coordinates x, y """

  def __init__(self, x_=0, y_=0):
    """ Create a new point at x, y """
    self.x = x_
    self.y = y_

  def distance_from_origin(self):
    """ Compute my distance from the origin """
    return((self.x ** 2) + (self.y ** 2)) ** 0.5
  def __add__(self, other):
    p=Point() # P1 is created
    p.x= self.x + other.x
    p.y= self.y + other.y
    return p