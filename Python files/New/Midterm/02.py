numbers = [ 951, 402, 984, 651, 360, 69, 408, 219, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165,
141, 501, 263, 617, 865, 575, 219, 390, 984, 592]


def GetEven(A): 
  newnumbers = []
  for number in A:
    if number != 219:
      if number%2 == 0:
        newnumbers.append(number)
    else:
      return newnumbers
  return newnumbers


print(GetEven(numbers))

print(55)