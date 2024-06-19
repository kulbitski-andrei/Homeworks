"""HOMEWORK 14.2"""

from cprint import cprint


def calculator(math_expression):
    """Accepts math expression and calculates it.
    Returns result of the calculation
    Can process most Errors and provide messages
    with explanation of what could be the reason of the Error"""
    try:
        math_expression = math_expression.replace(" ", "")
        result = eval(math_expression)
        return result

    except ZeroDivisionError:
        cprint.fatal("Деление на ноль: "
                     "В выражении применяется деление на ноль, "
                     "что не является допустимым действием\n")

    except NameError:
        cprint.fatal("Ошибка в выражении: "
                     "Убедитесь, что введенное выражение содержит "
                     "только числа, связанные математическими операторами\n")

    except SyntaxError:
        cprint.fatal("Ошибка в выражении: "
                     "Убедитесь, что введенное выражение содержит "
                     "только числа, связанные математическими операторами\n")

    except TypeError:
        cprint.fatal("Неверный тип данных: "
                     "Тип полученных данных не соответствует "
                     "числовому и не может быть обработан программой\n")

    return "Произошла ошибка, повторите ввод"


# TEST CASES
assert calculator("5 + 4 9") == 54
assert calculator("10 - 3 + 1 8") == 25
assert calculator("2 ** 3 - 1 7") == -9

assert not calculator("2 ** 3 - 17") == 100

print(calculator(input("Пожалуйста, введите математическое выражение, "
                       "которое Вы хотите вычислить...")))
