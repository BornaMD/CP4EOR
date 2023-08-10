##0
#class Test:
#  def __init__(self):
#    self.x=1
#  def getX(self):
#    return self.x
#t=Test()
#print("t.x is equal to: ",t.x)
#print("t.getX is equal to: ",t.getX())
#t.x=5
#print("----")
#print("t.x is equal to: ",t.x)
#print("t.getX is equal to: ",t.getX())
#
#class Test:
#  pass
#
#
#t1=Test()
#t1.attr=12
#print("t1.attr is equal to: ",t1.attr)
#t2=Test()
#print("t2.attr is equal to: ",t2.attr)

class Test:
  def __init__(self):
    self.x=1
    self.__y=1
  def getX(self):
    return self.x
  def getY(self):
    return self.__y


t=Test()
t.x=45 #45
t.__y=45 #nothing, no access 
print("t.x is equal to: ",t.x) # 45
print("t.getX is equal to: ",t.getX()) #45
print("t.__y is equal to: ",t.__y) #AttributeError:
print("t.getY is equal to: ",t.getY()) # 45
t._Test__y=45 #Access -> 45
print("t.getY is equal to: ",t.getY()) #45


