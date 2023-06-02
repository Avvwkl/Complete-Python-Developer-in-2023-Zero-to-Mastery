# print highest even
# even 0 2 4 6 8

# solution 1
def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)

print(highest_even([10,2,22,3,16,4,8,11]))