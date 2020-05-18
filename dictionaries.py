# Dictionary - is an unordered key value pair

dictionary = {
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True
}

my_list = [
    {
        'a': [1, 2, 3],
        'b': 'hello',
        'x': True
    },
    {
        'a': [4, 5, 6],
        'b': 'world',
        'x': False
    }

]

user = dict(name='Carlo')

print(dictionary)
print(dictionary['b'])
print(my_list[1]['a'][2])

print(dictionary.get('age', 55))
print(user)
print('a' in dictionary)
