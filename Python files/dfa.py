






nums=[1, 2, 3, 4, 5, 6, 9, 12, 1, 23, -3, 5, 6, 7]
newnums = []
total = 0

for i in range(len(nums)):
  if int(nums[i])>0:
    newnums.append(nums[i])

for i in range(len(newnums)):
  total += int(newnums[i])

avarage = total/len(newnums)

print('Average of positive integers: ', avarage)

nums=[1, 2, 3, 4, 5, 6, 9, 12, 1, 23, -3, 5, 6, 7]

newnums = []

for i in range(len(nums)):
  if int(nums[i])>0:
    newnums.append(nums[i])


total = 0

for i in range(len(newnums)):
  total += int(newnums[i])

average = total/len(newnums)

print("Average of positive integers: ", average)