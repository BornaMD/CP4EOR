def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-0.5)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
# Ask how this works?? and what it does exaclty. 
# Recursion means that you continue your calculations with the awnser of the calculation before. 
