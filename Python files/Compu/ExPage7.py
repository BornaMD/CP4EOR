# packs
import re

# Examples
m = re.search('(?<=abc)def', 'abcdef')
m.group(0)


# a

def checkHttp(input):
    input = str(input("Please provide a string to be checked for links: "))
    prog = re.compile(pattern=str)
    result = prog.match(string=input)
    print(result)


checkHttp('This is the text to be searched for occurrences of the http:// pattern.')
