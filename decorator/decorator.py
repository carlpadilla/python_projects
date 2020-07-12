# Decorator


def my_decorator(func):
    def wrap_func():
        print("*" * 14)
        func()
        print("*" * 14)

    return wrap_func


@my_decorator
def hello():
    print('Hello World!')


@my_decorator
def bye():
    print('Byeee!')


hello()
bye()
