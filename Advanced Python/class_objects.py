#OOP

class playercharacter:
    def __init__(self, name, age):
        self.name = name #attributes
        self.age = age

    def run(self):
        print('run')
        return 'done'

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2
    
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2
    
print(playercharacter.adding_things(2,3))
print(playercharacter.adding_things2(2,3))

player1 = playercharacter('Cindy', 44)
player2 = playercharacter('Tom', 21)



print(player1.run())
print(player2.age) 