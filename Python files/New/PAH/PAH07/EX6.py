def sum(list):
  sum = 0
  # Add every number in the list.
  for i in range(0, len(list)):
    sum = sum + list[i]
  # Return the sum.
  return sum
print(sum([5,7,3,8,10]))

def sum(list): 
  if len(list) == 1:
    return list[0]
  else: 
    return list[0] + sum(list[1:])

print(sum([5,7,3,8,10]))

