from functools import reduce

print('#1')
# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def uppercase(names):
    return str(names.upper())


print(list(map(uppercase, my_pets)))

print('#2')
# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

sorted_num = sorted(my_numbers)

print(list(zip(my_strings, sorted_num)))

print('#3')

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def check_if_over_50(i):
    return i > 50


print(list(filter(check_if_over_50, scores)))

print('#4')

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?


def accumulator(acc, item):
    # print(acc, item)
    return acc + item


print(reduce(accumulator, (my_numbers + scores), 0))
