# oop


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'Hi my name is {self.name} and I\'m {self.age} years old. ')


player1 = PlayerCharacter('Carl', 34)

player1.speak()
