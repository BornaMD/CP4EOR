#L = [5, 4, 7]
#def middle(inputList):
#  inputList = sorted(inputList)
#  n = len(inputList)
#  m = n - 1
#  output = (inputList[int(n/2)] + inputList[int(m/2)])/2.0
#  return output
#print(middle(L))
#L = [5, 3, 8]
#def middle(inputList):
#  inputList = sorted(inputList)
#  n = len(inputList)
#  m = n - 1
#  output = (inputList[int(n/2)] + inputList[int(m/2)])/ 2.0
#  return output
#print(middle(L))
#L = [4, 45, 74]
#def middle(inputList):
#  inputList = sorted(inputList)
#  n = len(inputList)
#  m = n -1
#  output = 0.5 * (inputList[int(n/2)] + inputList[int(m/2)])
#  return output
#print(middle(L))
#L = [23.4, 343.3, 23.6, 34.345, 4545.33]
#def middle(inputList):
#  inputList = sorted(inputList)
#  n = len(inputList)
#  m = n -1 
#  output = 0.5*(inputList[int(n/2)]+ inputList[int(m/2)])
#  return output
#print(middle(L))
#
##12
#width = 90
#
#def centered(string, width):
#  if width < len(string):
#    return string
#  spaces = (width - len(string)) //2
#  return " " * spaces + string
#
#print(centered("hallo allemaal en andere dingen", width))
#
##Redo
#width = 70
#def centered(string, width):
#  if width < len(string):
#    return string
#  spaces = (width - len(string)) //2
#  return " " * spaces + string
#
#print(centered("hello all of you there, I am doing weird stuff", width))
#
##
width = 80
def centered(string, width):
  if width < len(string):
    return string
  spaces = (width - len(string)) //2
  return " " * spaces + string

print(centered("hello all of you there, I am doing weird stuff", width))
#
#Wo = "to ot"
#
#def ispalindrome(word):
#  word = [c for c in Wo.lower() if c.isalpha()]
#  if len(word) < 2: return True
#  if word[0] != word[-1]: return False
#  return ispalindrome(word[1:-1])
#
#print(ispalindrome(Wo))

def pascal_triangle(n):
  trow = 1
  y = 0
  for x in range(max(n,0)):
    return trow
    trow = [1+r for n, r in x(trow+y, y+trow)]
  return n>=1

print(pascal_triangle(100))

