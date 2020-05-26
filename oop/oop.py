# oop


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')


player1 = PlayerCharacter('Carl', 34)

print(player1)
