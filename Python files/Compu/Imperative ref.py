

#from Metaclasses import Philosopher1, Philosopher2, Philosopher3
#
#
#plato = Philosopher1()
#kant = Philosopher2()
## let's see what Plato and Kant have to say :-)
#if required:
#    print(kant.the_answer())
#    print(plato.the_answer())
#else:
#    print("The silence of the philosphers")

from Metaclasses_ex import LittleMeta

class S:
  pass
class A(S, metaclass=LittleMeta):
  pass
a = A()
