# map, filter, zip and reduce

""" map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)"""

my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2


print(list(map(multiply_by2, my_list)))
print(my_list)

# filter - The filter() method constructs an iterator from elements of an iterable for which a function returns true.

""" In simple words, the filter() method filters the given iterable with the help of a function that tests each element in the iterable to be true or not.

The syntax of filter() method is:

filter(function, iterable)"""


def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))
print(my_list)
