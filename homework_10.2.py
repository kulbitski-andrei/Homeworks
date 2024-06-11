"""HOMEWORK #10.2"""


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
assert funny_numbers(-1, 0, 100, 200, 300)
assert funny_numbers(5.3, 0.8)
assert not funny_numbers(10, "abcd", 20)
