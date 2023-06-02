## Dictionary
# Data type in Python but its also a data structure
# ogranize our data


# key:value
print('\n---key:value---')
dictionary = {
    'a': 1,
    'b': [1,2,3],
    'x': 'hello',
    'z': True
}

print(dictionary['b'])
print(dictionary['b'][1])

print(dictionary)

# List example
print('\n---List example---')
my_list = [
    {
    'a': 1,
    'b': [1,2,3],
    'x': 'hello',
    'z': True
    },
    {
    'a': 1,
    'b': [4,5,6],
    'x': 'hello',
    'z': True
}
]

print(my_list[0]['b'][2])

# Keys
# Dictionary Key cannot change
# Dictinary Key has to be unique
print('\n---Keys---')
dictionary = {
    123: [1,2,3],
    True: 'hello',
    'z': True
}

print(dictionary[123])
print(dictionary[True])

# Dictionary Methods
# https://www.w3schools.com/python/python_ref_dictionary.asp
print('\n---Dictionary Methods---')

user = {
    'basket': [1,2,3],
    'greet': 'hello'
}

print(user.get('age')) # check if doesn't exists show none
print(user.get('age', 55)) # check if doesn't exists,otherwise use 55

print('basket' in user) # show true or false
print('basket' in user.keys()) # check in keys array
print('basket' in user.values()) # check in values array

print( user.items())

#print(user.clear())

user2 = user.copy() # copy the dictionary

print(user.pop('greet')) # remove the value
print(user.popitem()) # remove last key:value

print(user.update({'greet': 'hola'})) # update, if doesn't exist ,it add it