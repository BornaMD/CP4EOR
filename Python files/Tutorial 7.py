# Excersise 11

from collections import OrderedDict
class Roman_number:
  def __init__(self,num):

    self.roman = OrderedDict()
    self.roman[1000] = "M"
    self.roman[900] = "CM"
    self.roman[500] = "D"
    self.roman[400] = "CD"
    self.roman[100] = "C"
    self.roman[90] = "XC"
    self.roman[50] = "L"
    self.roman[40] = "XL"
    self.roman[10] = "X"
    self.roman[9] = "IX"
    self.roman[5] = "V"
    self.roman[4] = "IV"
    self.roman[1] = "I"

  def roman_num(num):
      for r in self.roman.keys():
        x, y = divmod(num, r)
        yield self.roman[r] * x
        num -= (r * x)
        if num > 0:
          roman_num(num)
        else:
          break

    return "".join([a for a in roman_num(num)])

num = int(input("Please enter a number: "))
print(Roman_number(num))

# Exercise 19
class clsString:
  def __init__(self):
    self.destring = ""
  def get_String(self):
    self.destring = input("give a string: ")
  def print_String(self):
    print(self.destring.upper())

s1=clsString()
s1.get_String()
s1.print_String()
