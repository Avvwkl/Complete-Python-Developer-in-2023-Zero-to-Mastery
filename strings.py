## Strings

print(type("hi hello"))
username = 'superhero'
password = 'superhero'
long_string = '''
WOW
O O
---
'''

print(long_string)


first_name = 'Bob'
last_name = 'Awk'
full_name = first_name + ' ' + last_name
print(full_name)

print('hello' + ' World') # string concatenation

# Escape Sequence
print('\n---Escape Sequence---')
weather = 'it\'s kind of sunny'
print(weather)

# Formatted Strings
print('\n---Formatted Strings---')
name = 'Johnny'
age = 50

print(f'hi {name}. You are {age} years old') # way to go - recommend
print('hi {}. You are {} years old'.format(name,age))
print('hi {1}. You are {0} years old'.format(name,age)) # Upside Down
print('hi {new_name}. You are {age} years old'.format(new_name='bob',age=100))

# String Indexes

print('\n---String Indexes---')
sell = '01234567'

print(sell[0:5]) # [start:stop]
print(sell[0:5:2]) # [start:stop:stepover]
print(sell[-2])
print(sell[::-1]) # reverse by 1


# Len - upper - capitalize - find - replace
# https://www.w3schools.com/python/python_ref_string.asp
# https://docs.python.org/3/library/functions.html
print('\n---Len etc---')
greet = 'hello'
print(greet[0:len(greet)])
print(len(greet))

# Booleans - True - False
print('\n--Booleans - True - False--')

print(bool(0))
print(bool(1))

# Comments
# https://realpython.com/python-comments-guide/
print('\n--Comments--')