def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    max, min = 0, float('Inf')
    for i in ints:
        if max < i:
            max = i
        elif i < min:
            min = i
    return (min, max)

## Example Test Case of Ten Integers
import random

l1 = [i for i in range(0, 50)]  # a list containing 0 - 9
random.shuffle(l1)
print ("Pass" if ((0, 49) == get_min_max(l1)) else "Fail")           # print Pass

l2 = [i for i in range(0, 2)]  # a list containing 0 - 9
random.shuffle(l2)
print ("Pass" if ((0, 1) == get_min_max(l2)) else "Fail")           # print Pass

l3 = [i for i in range(0, 79)]  # a list containing 0 - 9
random.shuffle(l3)
print ("Pass" if ((0, 78) == get_min_max(l3)) else "Fail")           # print Pass

l4 = [i for i in range(0, 6)]  # a list containing 0 - 9
random.shuffle(l4)
print ("Pass" if ((0, 5) == get_min_max(l4)) else "Fail")           # print Pass

l5 = [i for i in range(0, 100)]  # a list containing 0 - 9
random.shuffle(l5)
print ("Pass" if ((0, 99) == get_min_max(l5)) else "Fail")           # print Pass