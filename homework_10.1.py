"""HOMEWORK #10.1"""


# 1. Положительные аргументы функции¶

def validate_arguments(func):
    """wrapper that checks if given function arguments
    are positive numbers"""

    def wrapper(*args):

        for element in args:
            if element < 0:
                raise ValueError
        return func(args)[0]

    return wrapper


@validate_arguments
def funny_values(*args):
    """This function just returns values that were provided as an arguments"""
    return args


# TEST CASES
assert funny_values(100, 200, 300) == (100, 200, 300)
assert funny_values(5, 0) is ValueError
assert funny_values(-1) is ValueError
