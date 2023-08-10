def countup(n): 
  if n >= 0: 
    countup(n-1)
    if n == 0:
      print("Blastoff! ")
    print(n)

countup(5)