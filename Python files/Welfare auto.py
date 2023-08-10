p = list()
D = list()
q = list()
C = list()
min_p = int(input("Please give in a minimal price to check for: "))
max_p = int(input("Please give in a maximal price to check for: "))
min_q = int(input("Please give in a minimal price to check for: "))
max_q = int(input("Please give in a maximal price to check for: "))

def d(min_p, max_p):
  for i in range(min_p, max_p+1):
    p[i] = i
  for in range(min_p, max_p+1):
    D[i] = 16 - p
  return 