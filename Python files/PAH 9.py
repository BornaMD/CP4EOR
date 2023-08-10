# 1 a
#def printHello():
#  print("Hello")
#a = printHello()

#2 
def outerFunction():
  global a
  a = 20
  def innerFunction():
    global a
    a = 30
    print ( 'a =' , a)
a = 10
outerFunction()
print('a =', a)
# a =20 ->c

#4
class Foo:
  def printLine(self, line='Python'):

    print(line)

o1=Foo()
o1.printLine('Java')
# Java
#5 a
#6 a
#7 d
#8 d
#9 b
#10 a
#11 104

# Excersise 11

from collections import OrderedDict
def RomanNumbers(num):
  roman = OrderedDict()
  roman[1000] = "M"
  roman[900] = "CM"
  roman[500] = "D"
  roman[400] = "CD"
  roman[100] = "C"
  roman[90] = "XC"
  roman[50] = "L"
  roman[40] = "XL"
  roman[10] = "X"
  roman[9] = "IX"
  roman[5] = "V"
  roman[4] = "IV"
  roman[1] = "I"

  def roman_num(num):
    for r in roman.keys():
      x, y = divmod(num, r)
      yield roman[r] * x
      num -= (r * x)
      if num > 0:
        roman_num(num)
      else:
        break
  return "".join([a for a in roman_num(num)])

num = int(input("Please enter a number: "))
print(RomanNumbers(num))

#num, roman, numbers, r = ["M", "CM", etc...], [1000, 900, 500, 400, 100, etc...], int(input("Put in the number: ")), ''
#for i in range(len(num)):
#  if num[i] == numbers[i], elif num == 0, else:
#    r += roman[i] and num-=numbers[i], print("the roman number will be:" , r), raise Exception("the number must be positive!")

#12 

from collections import OrderedDict
def RealNumbers(letr):
  roman = OrderedDict()
  roman["M"] = 1000
  roman["CM"] = 900
  roman["D"] = 500
  roman["CD"] = 400
  roman["C"] = 100
  roman["XC"] = 90
  roman["L"] = 50
  roman["XL"] = 40
  roman["X"] = 10
  roman["IX"] = 9
  roman["V"] = 5
  roman["IV"] = 4
  roman["I"] = 1

  def roman_num(letr):
    for r in roman.values().strip().split(""):
      x, y = divmod(letr, r)
      yield roman * x
      letr -= (r * x)
      if letr.value() > 0:
        roman_num(letr)
      else:
        break
  return "".join([a for a in roman_num(letr)])

letr = int(input("Please enter a number: "))
print(RealNumbers(letr))

#Redo

#13

from schema import Shema, And, Use, Optional, ShemaError

class Validity:
  def __init__(self):
    def valParentheses(self):
      self = self.strip()
      if (self % 2) == 0:
        flow = self/2
        for a in range(len(flow)):
          prt1, prt2 = string[:len(self)/2], string[len(self)/2]
          return prt2 = reversed(prt2)
          if (self[a] == self[:a]):
            return
      else:
        return False


# Exercise 14
lst1 = list(input("Please give indices of two numbers: "))
trgtnum = int(input("Please give the target number a pair of elements in ", lst1, " should sum up to."))
parameter_LIST = lst1, trgtnum

class Sumtarget:
  def __init__(self, parameter_LIST):
      for i in range(lst1):
        lst1[i] = lst1[i.split("")]
        if (lst1[i] + lst1[i+1]) == trgtnum:
          return lst1[i]
          break
        elif (lst1[i] + lst1[i+1]) != trgtnum:
          i+=2
        else:
          raise Exception("Please give only two number indices in this string.")

print("The correct pair of elements is: ", )