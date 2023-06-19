class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return self
    
    def speak(self):
        print(f'my name is {self.name}, and I am')
player1 = PlayerCharacter('andrei', 100)

print(player1.name)
print(player1.age)
print(player1.run())