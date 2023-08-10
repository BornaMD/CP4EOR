nr=int(input('input a number: '))
van=int(input("van nummer: "))
tot=int(input("tot nummer: "))

def mt(nr,van,tot):
  for i in range(van,tot+1):
    print(str(nr) + ' x ' + str(i) + ' = ' + str(nr*i))

print(mt(nr,van,tot))