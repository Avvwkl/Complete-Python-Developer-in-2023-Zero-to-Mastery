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