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

"""
O(n^2) - Quadratic Time

Note how we now have two loops, one nested inside another. This means that for a list of n items, we will have to 
perform n operations for every item in the list! This means in total, we will perform n times n assignments, 
or n^2. So a list of 10 items will have 10^2, or 100 operations. You can see how dangerous this can get for very 
large inputs! 

"""


def func_quad(lst):
    """
    Prints pairs for every item in the list.
    :param lst:
    :return:
    """

    for item_1 in lst:
        for item_2 in lst:
            print(item_1, item_2)


print('Quadratic Time')
func_quad(lst)

