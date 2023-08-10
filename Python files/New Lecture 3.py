import timeit as ti

try:
  m=int(input("Develop multiplication table for:"))
except Exception:
  print("Oops!That was no valid number. Please try again.")
  m=int(input("Develop multiplication table for:"))
MaxSize= len(str(m*m))
for j in range(1,m+1):
  s=""
  for i in range (1,m+1):
  k=str(i*j)
  s+= k + " " * (1+MaxSize-len(k))
print (s)

try:
  #line1
  #line2 -> value error
  #line3 -> index error
  #line4 -> type error
except Exception:
  print("Something went wrong. Contact the admin!")


i=0

try:
  #line1
  #line2 -> value error
  #line3 -> index error
  #line4 -> type error

except ValueError:
  raise ValueError('This is the wrong value.')
except IndentationError:
  raise IndentationError('The intendation does not conform to the standards. ')  
if ti.timeit() >= 
except RuntimeError:
  raise RuntimeError('The runtime exceeds your expected lifespan. hèhèhè... *Evil eyes*')
except Exception:
  print("Something went wrong. Contact the admin!")


i=0
