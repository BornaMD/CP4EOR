class Circle(object):
  def __init__(self, circleNum):
    cn=0
    fh=open("geo.txt", "r")
    l =fh.readlines() #Not readable, name tha variables what they are to explain better to other programmers what the varable is used for.
    for i in l:
      if "Circle" in i:
        if cn == circleNum:
          self.__index = l.index(i) # Using index is slower than using idx and idx += 1
          self.__radius= l[self.__index][7] # Assumes that the radius is an integer. 
        else:
          cn+=1
    self.__l = l
    fh.close()
    
  @property
  def radius(self):
    return self.__radius

  @radius.setter
  def radius(self, radius):
    if radius < 0:
      raise ValueError("Radius has to be positive.")
    self.__radius = radius
    self.__save()

  def __save(self):
    self.__l[self.__index] = "Circle" + str(self.__radius) + "\n"
    fh=open("geo.txt", "w")
    for i in self.__l:
      fh.write(i)
    fh.close()

c1 = Circle(1)
print(c1.radius)
c1.radius = 3
print(c1.radius)
c1.radius = -2
print(c1.radius)
