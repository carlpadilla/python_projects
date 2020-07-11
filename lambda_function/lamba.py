# lambda expressions

my_list = [5, 4, 3]


# def multiply_by2(item):
#     return item * 2


# Multiplies by 2
print(list(map(lambda parameter_list: parameter_list * 2,  my_list)))
print(my_list)

# my_list squared
print(list(map(lambda parameter_list: parameter_list ** 2, my_list)))
