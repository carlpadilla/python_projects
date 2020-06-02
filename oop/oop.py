# oop


class PlayerCharacter:
    # class object attribute - static

    membership = True

    def __init__(self, name, age):
        if age < 18:
            self.name = name  # attributes
            self.age = age
        else:
            print('Player is not old enough.')

    def greet(self):
        print(f'my name is {self.name}')


player1 = PlayerCharacter('Carl', 10)
player2 = PlayerCharacter('Jenny', 29)
player2.attack = 50

print(player1.greet)
# print(player2.attack)
# print(player1.membership)
# print(player1.greet())
