# if statement

is_old = True
is_licenced = True

if is_old and is_licenced:
    print('You are old enough')
else:
    print('You are not of age')


# Truthy and Falsy
# https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false

#>>> bool([])
#False
#>>> bool([1])
#True
#>>> bool('')
#False
#>>> bool('hello')
#True

username = 'bob'
password = '123'

if username and password:
    print('You are old enough')
else:
    print('You are not of age')
