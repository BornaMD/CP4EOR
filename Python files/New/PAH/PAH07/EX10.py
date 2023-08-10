def sum_even(n):
  total = 0
  if n == 0:
    return total
  elif n != 0: 
    total =  sum_even(n-2)
    return total 

sum_even(5)
