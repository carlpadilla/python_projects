"""O(1) - Constant time Note how this function is constant because regardless of the list size, the function will
only ever take a constant step size, in this case 1, printing the first value from a list. so we can see here that an
input list of 100 values will print just 1 item, a list of 10,000 values will print just 1 item, and a list of n
values will print just 1 item! """


def func_constant(values):
    val = values[0]
    print(val)


lst = [1, 2, 3, 4, 5, ]
print("Constant Time")
func_constant(lst)

"""# O(n) - Linear time This function runs in O(n) (linear time). This means that the number of operations taking 
place scales linearly with n, so we can see here that an input list of 100 values will print 100 times, a list of 10,
000 values will print 10,000 times, and a list of n values will print n times. 

"""


def func_lin(values):
    for val in lst:
        print(val)


print("Linear Time")
func_lin(lst)
