# List example

basket = [1, 2, 3, 4, 5]

# adding
basket.append(100)  # modifies the list in place
# new_list = basket

# print(new_list)
print(basket)


# removing
basket.pop()
print(basket)


# index
print(basket.index(2))  # number 2 is at the index of 1

# sorted list

letters = ['a', 'b', 'c', 'd', 'x', 't', 'g']

# letters.sort() # Sorts the original list

print(sorted(letters))  # sorts items in list and produces a new list.

print(letters)

# generates a list from 0-100
print(list(range(101)))

# join
sentence = ' '.join(['hi', 'my', 'name', 'is', 'carl'])
print(sentence)

# list unpacking
a, b, c, *other, d = 1, 2, 3, 4, 5, 6, 7, 8, 9

print(a)
print(b)
print(c)
print(other)
print(d)
