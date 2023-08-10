# Question 12
fh=open("words.txt", "r+")
words = str(fh.readlines()).rstrip()
characters = 'abcdefghijklmnopqrstuvwxyz'.split()
words = words.lower()
char = {}
for ch in 'abcdefghijklmnopqrstuvwxyz':
  char[ch] == 0

print(characters)
print(words)
#for i in range(len(words)):
#  if i == 

# Exercise 21
fh=open(input("Give the name of the file + its extention: [e.g. filename.txt] "), "r+")
word_list = str(fh.readlines()).rstrip().split(input("The file is seperated by: "))

def find_longest_word(word_list):  
  longest_word =  max(word_list, key=len)
  return longest_word

print(find_longest_word(word_list))

fh.close()

#Exercise 22
import os

def getSize(filename):
  st = os.stat(filename)
  return st.st_size

f = input("Give the name of the file + its extention: [e.g. filename.txt] ")

print("The file " + str(f) + " is " + str(getSize(f)) + " bytes.")

#if getSize(f) > 1000


#f = input( )
#if getSize(f)> limit:

# Exercise 12 (review)
message = "hello world"
d = {}
letters = set(message)
for l in letters:
    d[message.count(l)] = l

print d[d.keys()[-1]], d.keys()[-1]