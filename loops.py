# loops
# iterable mean loop something
print('\n---loops---')

for item in 'Zero to Mastery': # 'Zero to Mastery' is iterable
    print(item)

# list
for item in [1,2,3,4,5]:
    print(item)

# set
for item in {1,2,3,4,5}:
    print(item)

# tuple
# set
for item in (1,2,3,4,5):
    print(item)

print('\n---loops in loop---')
for item in (1,2,3,4,5):
    for x in ['a', 'b', 'c']:
        print(item, x)


# range()
print('\n---range---')

for number in range(0, 100):
    print(number)

for number in range(0, 100, 2):
    print(number)