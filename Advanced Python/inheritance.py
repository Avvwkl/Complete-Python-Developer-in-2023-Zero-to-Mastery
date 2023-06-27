# inheritance mean give access in class to another
# with (User), wizard and archer will be execute with User class

class User:
    def sign_in(self):
        print('logged in')
        
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack():
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack():
        print(f'attacking with arrows: arrows left -  {self.num_arrows}')


wizard1 = Wizard()
print(wizard1.sign_in())