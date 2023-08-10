class Point:

  """ Point class represents and manipulates x,y coords. """
  def __init__(self, x=0, y=0):

    """ Create a new point at x, y """

    self.x = x

    self.y = y

 		
def midpoint(p1, p2):

  """ Return the midpoint of points p1 and p2 """
  mx = (p1.x + p2.x)/2
  my = (p1.y + p2.y)/2
  return Point(mx, my)
 		

p1=Point(x=4, y=8)
p2=Point(x=2, y=4)

print(midpoint(p1, p2))
print(Point())