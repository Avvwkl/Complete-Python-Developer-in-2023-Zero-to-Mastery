# Exercise: Check for duplicates in list:

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# Solution 1

newlist =[]
duplist = []

for i in some_list:
    if i not in newlist:
        newlist.append(i)
    else:
        duplist.append(i)

print(duplist)

# Solution 2

duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)