# while
print('\n---While---')
i = 0
while i < 50:
    print(i)
    i += 1
else:
    print('done with all the work')


# break
print('\n---break---')
i = 0
while i < 50:
    print(i)
    i += 1
    break
else:
    print('done with all the work')

# for and while
print('\n---for and while---')

my_list = [1,2,3]
for item in my_list:
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1


# while True:
print('\n---While True---')

while True:
    response = input('say something: ')
    if (response == 'bye'):
        break

# break, continue, pass
# continue go the loop from start
print('\n---break, continue, pass---')

my_list = [1,2,3]

i = 0
while i < len(my_list):
    i += 1
    continue
    print(my_list[i])



for item in my_list:
    # thinking about it
    pass
