# Functions
# Should do one thing realy well
# Should return something

print('\n---Functions---')

def say_hello():
    print('Hello')

say_hello()

# Parameters - define
print('\n---Parameters - Position Arguments---')

def say_hello2(name, emoji):
    print(f'Helooo {name} {emoji}')

# positional argumets - call - invoke
say_hello2('Bob', '😁')



# keyword arguments
print('\n---Keyword Arguments---')

say_hello2(emoji='😁', name='Awk')

# Default Parameters
print('\n---Default Parameters---')

def say_hello2(name='Darth Vader', emoji='😈'):
    print(f'Helooo {name} {emoji}')

say_hello2()
say_hello2('Bob2')

# return
print('\n---return---')

def sum(num1, num2):
    return num1 + num2

total = sum(10,5)
print(total)


def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)

total = sum(10,5)
print(total)

# Docstring # add info inside the function
# help find what function does with info
# .__doc__ same
def test(a):
    '''
    info:
    '''
    print(a)

test(5)
#help(test)
print(test.__doc__)