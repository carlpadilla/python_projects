class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'jimmy',
            'has_pets': False
        }

    def __str__(self):
        return f'{self.color}'

    def __call__(self):
        return 'called!'

    def __getitem__(self, item):
        return self.my_dict[item]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(action_figure())
print(action_figure['name'])
