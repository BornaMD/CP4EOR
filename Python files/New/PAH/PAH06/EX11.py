val1 = int(input("Please provide the first numerical value: "))
val3 = int(input("Please provide the first numerical value: "))
val2 = int(input("Please provide the first numerical value: "))


def med_val(val1, val2, val3):
  l = [val1, val2, val3]
  li = sorted(l)
  return li[1]

print(med_val(val1, val2, val3))

