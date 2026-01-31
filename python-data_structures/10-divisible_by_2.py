#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Return a list of True/False if elements are multiples of 2."""
    return [num % 2 == 0 for num in my_list]
