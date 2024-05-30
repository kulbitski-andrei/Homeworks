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
print("Task 1")
print(solution([1, 2, 3]))  # Expected True
print(solution([1, 2, 1, 2]))  # Expected False
print(solution([1, 3, 2, 1]))  # Expected False
print(solution([1, 2, 3, 4, 5, 3, 5, 6]))  # Expected False
print(solution([40, 50, 60, 10, 20, 30]))  # Expected False

# print(solution([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))  # Expected True
# print(solution([1, 2, 3, 1, 2, 3]))  # Expected Fasle
# print(solution([1, 1]))  # Expected True
# print(solution([100, 105, 120, 110, 140, 170]))  # Expected True
# print(solution([100, 105, 120, 110, 140, 170, 150]))  # Expected False
# print(solution([100, 1, 2, 3, 4, 5]))  # Expected True
# print(solution([1, 2, 3, 4, 5, 100]))  # Expected True


# 2. Число напротив¶

def numeric_circle(n, first_number):
    """Accepts circle size(n) and first number's position
    on a numeric circle.
    Returns opposite number position on a numeric circle."""

    distance = n / 2  # Distance between numbers

    if first_number >= distance:
        second_number = first_number - distance
    else:
        second_number = first_number + distance

    return int(second_number)


print("\nTask 2")
print(numeric_circle(10, 2))


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

    # print(control_summ)

    if control_summ % 10 != 0:
        return False

    return True


print("\nTask 3")
print(validate(4561261212345464))  # False expected
print(validate(4561261212345467))  # True expected

# print(validate(1111111111111111))  # False expected
# print(validate(4561261212345461))  # False expected
# print(validate(378282246310009))  # False expected
# print(validate(378282246310005))  # True expected (American Express)
# print(validate(5610591081018250))  # True expected (Australian BankCard)
# print(validate(6011000990139424))  # True expected (Discover)
# print(validate(5555555555554444))  # True expected (MasterCard)
# print(validate(4012888888881881))  # True expected (Visa)
# print(validate("aaaaaa"))  # "Wrong input!" expected
# print(validate(""))  # "Wrong input!" expected
# print(validate(724708))  # True expected
# print(validate(555))  # False expected
# print(validate(validate(100)))  # "Wrong input!" expected
