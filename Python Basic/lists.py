## Lists = ~array
# Data Structure (Organize information)

li = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li3 = [1,2.5,'a', True]

# List slicing
# [:]
print('\n---List slicing---')
eshop_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

print(eshop_cart[0:2])
print(eshop_cart[0::2])

eshop_cart[0] = 'laptop'
print(eshop_cart)

new_cart = eshop_cart[:] # copy the eshop_cart
new_cart = eshop_cart # connect/modify the old list and with the new


# Matrix
print('\n---Matrix---')
matrix = [
    [1,5,1],
    [0,1,0],
    [1,0,1]
]

print(matrix[0][1])

# List Methods
print('\n---List Methods---')
# https://www.w3schools.com/python/python_ref_list.asp
# https://www.w3schools.com/python/python_ref_keywords.asp
# Modify the lists in place, dont copy the list
# append - insert - extend - remove
# adding
print('\n---adding---')
basket = [1,2,3,4,5]
basket.append(100)
basket.insert(5,100)
basket.extend([101])
new_list = basket
print(new_list)
print(basket)

# removing
print('\n---removing---')
basket = [1,2,3,4,5]
basket.pop()
basket.pop(0) # place of 0
basket.remove(4) # value of 4
basket.clear() # clear the list
print(basket)

# index
print('\n---index---')
basket = ['a','b','c','d','e']
print(basket.index('c'))
print(basket.index('d', 0, 4))
print('d' in basket)
print(basket.count('d'))

basket.sort()
print(basket)
print(sorted(basket)) # create a new copy of the list and sorted

new_basket = basket.copy()
basket.reverse()
print(basket)

print(list(range(100))) # generate a list

# Join
print('\n---Join---')

new_sentence = ' '.join(['hi','my','name','is','JOJO'])
print(new_sentence)

# List unpacking
print('\n---List unpacking---')

a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]

print(a)
print(b)
print(c)
print(other)
print(d)
