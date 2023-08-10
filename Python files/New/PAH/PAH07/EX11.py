L = [4,5,6,4,6,3,6,37,43,75]
#
#def prod(L):
#  product, i = 1,0
#  while i < len(L):
#    product = product * L[i]
#    i = i + 1
#  return product
#
#prod(L)
#

def prod2(L):
#  global i
  product = 0
  if len(L) == 0:
    print(product)
    break
  elif len(L) > 0: 
    product = L[-1] * L[-2] 
    del L[-1]
#    i+=1
    print(product)
  else: 
    raise ValueError

#i = 0
prod2(L)
#prod(L)