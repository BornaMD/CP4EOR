class dictObj(object):
    def __init__(self):
        self.x='red'
        self.y='Yellow'
        self.z='Green'
    def do_nothing(self):
        pass
test=dictObj()
print(test.__dict__)

n=int(input("max n: "))
d=dict()

for x in range(1, n+1):
    d[x]=x**2
print(d)

# Binary Search
list_search_criteria = list(input("Give in the list for search: ").split(","))
search_value = int(input("Give in the value to be searched for: "))

def binary_search(item_list, item):
    first=0
    last=len(item_list)-1
    found=False
    while(first<=int(last and not found)):
        mid=(first+last)//2
        if item_list[mid] == item:
            found=True
        else:
            if item<item_list[mid]:
                last=mid-1
            else:
                first = mid+1
    return found
print(binary_search(list_search_criteria, search_value))

# Seqental search

list_parameters = list([input("List with the parameters: ")])
Search_value = int(input("Value to search for: "))


def Sequental_Search(dlist, item):
    pos = 0
    found = False

    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else: 
            pos=pos+i
    return found, pos

print(Sequental_Search(list_parameters, Search_value))

# Counting Sort

def counting_sort(array1, max_value):
    m=max_value+1
    count=[0]+m

    for a in array1:
        count[a]+=1
    i=0
    for a in range(m):
        for c in range(count[a]):
            array1[i]=a
            i+=1
    return array1

    
print(counting_sort(list(input("Put in the list with occurancas: ")), int(input("Maximal Value: "))))
