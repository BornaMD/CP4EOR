while True:
    try:
        m=int(input("Develop multiplication table for:"))
        if(m>0):
            break
        else: #stay in the loop
            print("Oops! The number should be positive. Please try again.")
    except Exception:
        print("Oops! That was no valid number. Please try again.")
MaxSize= len(str(m*m))
for j in range (1,m+1):
    s=""
    for i in range (1,m+1):
        k=str(i*j)
        s+= k + " " * (1+MaxSize-len(k))
    print(s)
    

for i in range(1,13):
    print(9*i)

i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 
10
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

if 5 > 2:
  print("Five is greater than two!")
#This is a comment.
print("Hello, World!")
"""This is a
multiline docstring."""
print("Hello, World!")
x = 5
y = "John"
print(x)
print(y)
x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)
x = "awesome"
print("Python is " + x)
x = "Python is "
y = "awesome"
z =  x + y
print(z)
x = 5
y = 10
print(x + y)

x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z)) 
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z)) 
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z)) 
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z)) 
print(x)
print(y)
print(z) 

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0' 
a = "Hello, World!"
print(a[1])
b = "Hello, World!"
print(b[2:5])
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
a = "Hello, World!"
print(len(a))
a = "Hello, World!"
print(a.lower())
a = "Hello, World!"
print(a.upper())
a = "Hello, World!"
print(a.replace("H", "J"))
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 



thistuple = ("apple", "banana", "cherry")
print(thistuple)
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))
thisset = {"apple", "banana", "cherry"}
print(thisset) 
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) 
thisset = set(("apple", "banana", "cherry"))
thisset.add("damson")
print(thisset) 
thisset = set(("apple", "banana", "cherry"))
thisset.remove("banana")
print(thisset) 
thisset = set(("apple", "banana", "cherry"))
print(len(thisset))

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
x = thisdict["model"]
x = thisdict.get("model")
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

for x in thisdict:
  print(x) 
for x in thisdict:
  print(thisdict[x])
for x in thisdict.values():
  print(x) 
for x, y in thisdict.items():
  print(x, y) 
print(len(thisdict)) 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict) 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict) 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict) 
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
if a > b: print("a is greater than b")
print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B") 
if a > b and c > a:
  print("Both conditions are True")
if a > b or a > c:
  print("At least one of the conditions are True")

c0 = 0.3
vector_c = [c0]*3

def p(Q):
    return 1 - Q

def costs(q,c):
    return c*q

def profits(q,Q_other,c):
    return p(q+Q_other)*q-costs(q,c)

def reaction(Q_other,c):
    q1 =  optimize.fminbound(lambda x: -profits(x,Q_other,c),0,1,full_output=1)
    return q1[0]

def fixed_point_three_firms(vector_q,vector_c):
    return [vector_q[0]-reaction(vector_q[1]+vector_q[2],vector_c[0]),
            vector_q[1]-reaction(vector_q[0]+vector_q[2],vector_c[1]),
            vector_q[2]-reaction(vector_q[0]+vector_q[1],vector_c[2])]

total_equilibrium_output = round(sum(optimize.fsolve(lambda q: fixed_point_three_firms(q,vector_c), vector_c)),3)
P0 = p(total_equilibrium_output)
H0 = (0.175/total_equilibrium_output)**2*3
print("Q: ", total_equilibrium_output)
print("P0: ", P0)
print("P0: ", H0)

def fixed_point_two_firms(q,c):
    return [q[0]-reaction(q[1],c[0]),q[1]-reaction(q[0],c[1])]
Individual_q_nr = optimize.fsolve(lambda q: fixed_point_two_firms(q,[0,0]), [0,0])

Individual_q = ['%.4f' % elem for elem in Individual_q_nr]
print(Individual_q)

initial_guess = [0,0]

c_after_merger = np.random.uniform(0,c0,size = 100)

q1_after_merger = [optimize.fsolve(lambda q: fixed_point_two_firms(q,[c0,c]), initial_guess)[0] for c in c_after_merger]
q2_after_merger = [optimize.fsolve(lambda q: fixed_point_two_firms(q,[c0,c]), initial_guess)[1] for c in c_after_merger]

c_after_merger = np.random.uniform(0,c0,size = 100)

q1_after_merger = [optimize.fsolve(lambda q: fixed_point_two_firms(q,[c0,c]), initial_guess)[0] for c in c_after_merger]
q2_after_merger = [optimize.fsolve(lambda q: fixed_point_two_firms(q,[c0,c]), initial_guess)[1] for c in c_after_merger]

df_after_merger['Q']= df_after_merger['output_non_merging_firm']+df_after_merger['output_merged_firm']
df_after_merger['P']= p(df_after_merger['Q'])
df_after_merger['H']= ((df_after_merger['output_non_merging_firm']/df_after_merger['Q'])**2+(df_after_merger['output_merged_firm']/df_after_merger['Q'])**2)
df_after_merger.head()

plt.hist(x=df_after_merger['P'],)
plt.vlines(P0,0,16)
plt.legend(['P0','Possible Price'])
plt.xlabel('$P$', fontsize=16)
plt.ylabel('Freq.', fontsize=16)
plt.xticks(np.arange(.43, .53, .01))
plt.title('The equilibrium price $P$', fontsize=20)
plt.show()

