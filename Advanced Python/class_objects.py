#OOP

class playercharacter:
    def __init__(self, name, age):
        self.name = name #attributes
        self.age = age

    def run(self):
        print('run')
        return 'done'

player1 = playercharacter('Cindy', 44)
player2 = playercharacter('Tom', 21)

print(player1.run())
print(player2.age)

#attributes and methods

class playercharacter:
    # class object attribute
    membership = True

    def __init__(self, name, age):
        if (self.membership): #(playercharacter.membership)
            self.name = name #attributes
            self.age = age

    def shout(self):
        print(f' my name is {self.name}')


player1 = playercharacter('Cindy', 44)

print(player1.membership)
print(player1.shout())