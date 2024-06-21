"""HOMEWORK #8"""


# 1. Последовательность¶

def solution(args):
    """Accepts array of numbers.
    If array is ascending or can be turned into ascending
    by deletion of one element in the array, returns True.
    In other cases returns False"""

    iteration_index = 0

    for _ in args:

        list_with_one_arg_deleted = list(args)
        list_with_one_arg_deleted.pop(iteration_index)

        if (list_with_one_arg_deleted == sorted(list_with_one_arg_deleted)
                and len(list_with_one_arg_deleted) ==
                len(set(list_with_one_arg_deleted))):
            return True

        iteration_index += 1

    return False


# TEST CASES
assert solution([1, 2, 3])
assert not solution([1, 2, 1, 2])
assert not solution([1, 3, 2, 1])
assert not solution([1, 2, 3, 4, 5, 3, 5, 6])
assert not solution([40, 50, 60, 10, 20, 30])


# 2. Число напротив¶

def numeric_circle(n, first_number):
    """Accepts circle size(n) and first number's position
    on a numeric circle.
    Returns opposite number position on a numeric circle."""

    distance = n / 2  # Distance between numbers

    if first_number >= distance:
        return int(first_number - distance)
    return int(first_number + distance)


# TEST CASES
assert numeric_circle(10, 2) == 7


# 3. Валидировать номер кредитной карты через алгоритм Луна

def validate(credit_card_input):
    """Accepts credit card number (int, any number of characters).
    Checks if credit card number is valid according to Luhn algorythm.
    Returns True if credit card number is valid.
    Rturns False if credit card number is invalid."""

    if not credit_card_input or not str(credit_card_input).isdigit():
        return "Wrong input!"

    credit_card_list = list(map(int, str(credit_card_input)))
    is_odd = True
    control_summ = 0

    for current_number in credit_card_list[::-1]:

        if not is_odd:
            current_number = current_number * 2

            if current_number > 9:
                current_number -= 9

        control_summ += current_number

        is_odd = not is_odd

    if control_summ % 10 != 0:
        return False

    return True


# TEST CASES
assert not validate(4561261212345464)
assert validate(4561261212345467)
