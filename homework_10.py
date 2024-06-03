"""HOMEWORK #10"""


# 1. Положительные аргументы функции¶

def validate_arguments(_):
    """wrapper that checks if given function arguments
    are positive numbers"""

    valid_message = "Valid input!"

    def wrapper(*args):

        for element in args:
            if element > 0:
                continue
            raise ValueError

        return valid_message

    return wrapper


@validate_arguments
def funny_values(*args):
    """This function just returns values that were provided as an arguments"""
    return args


# TEST CASES
assert funny_values(100, 200, 300) == "Valid input!"
# assert funny_values(5, 0) == ValueError
# assert funny_values(-1) == ValueError


# 2. Вернуть число¶

def validate_instance(_):
    """wrapper that checks if given function arguments
    are int or float numbers"""

    valid_message = "Valid input!"
    invalid_message = "Invalid input!"

    def wrapper(*args):

        for element in args:
            if isinstance(element, (int, float)):
                continue
            return invalid_message

        return valid_message

    return wrapper


@validate_instance
def funny_numbers(*args):
    """This function just returns values that were provided as an arguments"""
    return args


# TEST CASES
assert funny_numbers(0, 100, 200, 300) == "Valid input!"
assert funny_numbers(5.3, 0.8) == "Valid input!"
assert funny_numbers(-1) == "Valid input!"
assert funny_numbers(10, "abcd", 20) == "Invalid input!"


def type_checker(_type):
    """Decorator that checks argument type and modify them if needed,
    so strings will concatenate and ints and floats
    will be added mathematically"""
    def wrapper(_):
        def inner(*args):

            if _type == str:
                summa = ""
                for i in args:
                    if i is None:
                        i = str("")
                    summa += str(i)
                return summa

            if _type == int:
                summa = 0
                for i in args:
                    if i is None:
                        i = 0
                    summa += int(i)
                return summa

            if _type == float:
                summa = 0
                for i in args:
                    if i is None:
                        i = 0
                    summa += float(i)
                return summa

            return None
        return inner
    return wrapper


@type_checker(_type=str)
def add(a, b, c=None):
    """dummy addition function example 1"""
    return a + b + c


@type_checker(_type=int)
def add2(a, b, c=None):
    """dummy addition function example 2"""
    return a + b + c


@type_checker(_type=float)
def add3(a, b, c=None):
    """dummy addition function example 3"""
    return a + b + c


# TEST CASES
assert add("3", 5) == "35"
assert add(5, 5) == "55"
assert add("a", "b") == "ab"

assert add2(5, 6, 7) == 18

assert add3(0.1, 0.2, 0.4) == 0.7000000000000001
