# Create file

f = open("file_for_recap.txt", 'w+')

# Parse text

text = f.read()

# Close file

f.close()

with open('file_for_recap.txt') as fobj:
  textr = fobj.read()

print(text)
print(textr)



try:
  with open("file_for_recap") as p:
    txt = p.read()
except FileNotFoundError:
  txt = None
print(txt)

