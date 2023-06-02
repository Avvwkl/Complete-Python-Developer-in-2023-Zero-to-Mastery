# Scope - what variables do i have access to?

a = 1

def parent():
    def confusion():
        return a
    return confusion()

print(parent())
print(a)


#1 - start with local
#2 - parent local # nonlocal
#3 - global
#4 - built in python functions

# Global

total = 0

def count():
    global total
    total += 1
    return total

print(count())

# Global 2

total = 0

def count(total):
    total += 1
    return total

print(count(1))
