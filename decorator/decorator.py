# Decorator


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("*" * 14)
        func(*args, **kwargs)
        print("*" * 14)

    return wrap_func


@my_decorator
def hello(greeting, emoji=':)'):
    print(greeting, emoji)


@my_decorator
def bye():
    print('Byeee!')


hello('Hello')
bye()
