"""HOMEWORK #10.3"""


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
