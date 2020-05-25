some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

a = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in a:
            a.append(value)

print(a)
