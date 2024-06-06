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

def validate_instance(func):
    """wrapper that checks if values returned by the function
    are numbers (int or float)"""

    valid_message = "Valid input!"
    invalid_message = "Invalid input!"

    def wrapper(*args):

        for element in func(args)[0]:

            if not isinstance(element, (int, float)):
                print(invalid_message)
                return False

        print(valid_message)
        return True

    return wrapper


@validate_instance
def funny_numbers(*args):
    """This function just returns values that were provided as an arguments"""
    return args


# TEST CASES
funny_numbers(-1, 0, 100, 200, 300)
funny_numbers(5.3, 0.8)
funny_numbers(10, "abcd", 20)


def type_checker(_type):
    """Decorator that checks argument type and modify them if needed,
    so strings will concatenate and ints and floats
    will be added mathematically"""
    def wrapper(_):
        def inner(*args):

            if _type == str:
                summa = ""
                for i in args:
                    summa += str(i)
                return summa

            if _type == int:
                summa = 0
                for i in args:
                    summa += int(i)
                return summa

            if _type == float:
                summa = 0
                for i in args:
                    summa += float(i)
                return summa

            return None
        return inner
    return wrapper


@type_checker(_type=str)
def add(a, b):
    """dummy addition function example 1"""
    return a + b


@type_checker(_type=int)
def add2(a, b, c):
    """dummy addition function example 2"""
    return a + b + c


@type_checker(_type=float)
def add3(a, b, c):
    """dummy addition function example 3"""
    return a + b + c


# TEST CASES
assert add("3", 5) == "35"
assert add(5, 5) == "55"
assert add("a", "b") == "ab"

assert add2(5, 6, 7) == 18

assert add3(0.1, 0.2, 0.4) == 0.7000000000000001
