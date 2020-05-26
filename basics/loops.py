# loops
for letter in 'Carl Padilla':
    print(letter)

# iterable - list, dict, tuple, set, string
# iterated -> one by one check each item in the collection

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim':  False
}

for item, value in user.items():
    print(item, value)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)