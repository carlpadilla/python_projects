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

    def arrows(self):
        print(f'attacking with arrows: arrows left {self.num_arrows}')

    def run(self):
        print('Ran really fast!')


class Elf(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
wizard1.attack()

Elf1 = Elf('carl', 100, 50)
print(Elf1.run())
print(Elf1.attack())
print(Elf1.arrows())
print(Elf1.sign_in())
