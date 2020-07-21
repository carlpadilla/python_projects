# list, set, dictionary

# my_list = []
# for char in 'hello':
#     my_list.append(char)

# set comprehension {}
my_list = {char for char in 'hello'}
# list comprehension []
my_list2 = [num for num in range(0, 100)]
my_list3 = [num ** 2 for num in range(0, 100)]
my_list4 = [num ** 2 for num in range(0, 100)
            if num % 2 == 0]

simple_dict = {
    'a': 1,
    'b': 2
}

# dict comprehension
my_dict = {key: value**2 for key, value in simple_dict.items()
           if value % 2 == 0}


print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)
print(my_dict)


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)

# print(duplicates)
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)
