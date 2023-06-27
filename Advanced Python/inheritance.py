# inheritance mean give access in class to another
# with (User), wizard and archer will be execute with User class

class User():
    def sign_in(self):
        print('logged in')
        
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left -  {self.num_arrows}')


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Bob', 100)


wizard1.attack()
archer1.attack()


print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, Archer))
#isinstance(isinstance, Class)





# Polymorphism

def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)