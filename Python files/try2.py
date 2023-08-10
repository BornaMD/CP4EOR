#def linereader(x,i):
#  if i > 0:
#    return (x[i] + "\n")
#  else:
#    raise Exception("The number of values is not positive. ")

#x, i = input("Please give the filename.txt and the amount of lines to be returned: ")


#fh=open("words.txt", "r+")
#y = fh.readlines()
#while x == len(y="\n"):
#  for i in range(x<11):
#    try: 
#      print("line " + i + ' = ' + fh.readline(linereader(i)))
#    except: 
#      if i not in range:
#        break


width = int(input(" Put in a width you would like the ... to be."))
def center(s, width):
  if width < len(s):
    return s
  spaces = (width - len(s)) // 2
  result = " "* spaces+s

  return result
def main():
  print(center("Some random stuff", width))
  print(center("by some random company:", width))
  print(center("Solving some random problem", width))
  print("\n")
  print(center("Copying some random stuff...", width))

main()

