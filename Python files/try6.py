# Excersise 11

from collections import OrderedDict
class Roman_number:
  def __init__(self,num):

    __self.roman = OrderedDict()
    __self.roman[1000] = "M"
    __self.roman[900] = "CM"
    __self.roman[500] = "D"
    __self.roman[400] = "CD"
    __self.roman[100] = "C"
    __self.roman[90] = "XC"
    __self.roman[50] = "L"
    __self.roman[40] = "XL"
    __self.roman[10] = "X"
    __self.roman[9] = "IX"
    __self.roman[5] = "V"
    __self.roman[4] = "IV"
    __self.roman[1] = "I"

  def roman_num(num):
      for r in __self.roman.keys():
        x, y = divmod(num, r)
        yield __self.roman[r] * x
        num -= (r * x)
        if num > 0:
          roman_num(num)
        else:
          break

  return "".join([a for a in roman_num(num)])

num = int(input("Please enter a number: "))
print(Roman_number(num))


num, roman, numbers, r = ["M", "CM", etc...], [1000, 900, 500, 400, 100, etc...], int(input("Put in the number: ")), ''
for i in range(len(num)):
  if num[i] == numbers[i], elif num == 0, else:
    r += roman[i] and num-=numbers[i], print("the roman number will be:" , r), raise Exception("the number must be positive!")
