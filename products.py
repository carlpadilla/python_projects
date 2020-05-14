

class Product:
    def __init__(self, name, price, in_stock=True, on_sale=False):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} costs {self.price}'


class Clothing(Product):
    def __init__(self, name, price, color):
        super().__init__(name, price)

        self.size = size
        self.color = color

    def __str__(self):
        super().__str__() + ' and has color {self.color} and size {self.size}'
