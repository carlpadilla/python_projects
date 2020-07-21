# interable
# iterable

# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i * 2)
#     return result


# my_list = make_list(100)
# print(list(range(100000)))


def generator_func(num):
    for i in range(num):
        yield i


for item in generator_func(10000):
    print(item)
