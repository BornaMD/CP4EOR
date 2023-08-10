#example 1
import math
from functools import lru_cache

@lru_cache(maxsize=1000)
def A(x):
  if x==1:
    A = 1
  elif x != 1:
    A = math.sqrt(6+A)
  B = []
  B[x] = A


@lru_cache(maxsize=1000)
def B(A):
  for i in range(0,1000):
    A(i)
    i +=i
    return B

print(B)