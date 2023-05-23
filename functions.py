# Functions
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
