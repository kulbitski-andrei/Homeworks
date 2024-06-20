"""HOMEWORK 14.2"""

# from cprint import cprint

"""Welcome to the Community version of Expression Calculator.
It supports such operations as exponentiation, multiplication, 
division, addition and subtraction. To unlock more operations
please consider purchasing Advanced or Pro version."""


def calculator_engine(expression):
    """Main function of the app that calls all other functions
    and handles different types of errors.
    Do not forget to provide a mathematical expression!"""

    # try:

    result = (convert_list_element_to_number
     (addition_subtraction
      (multiplication_division
       (exponentiation
        (convert_expression_to_list(expression))))))

    return result

    # except ZeroDivisionError:
    #     cprint.fatal("Division by zero: "
    #                  "The expression uses division by zero, "
    #                  "which is not a valid operation\n")
    #
    # except NameError:
    #     cprint.fatal("Error in the expression: "
    #                  "Make sure the entered expression contains "
    #                  "only numbers connected by mathematical operators\n")
    #
    # except SyntaxError:
    #     cprint.fatal("Error in the expression: "
    #                  "Make sure the entered expression contains "
    #                  "only numbers connected by mathematical operators\n")
    #
    # except TypeError:
    #     cprint.fatal("Incorrect data type: "
    #                  "The type of the received data does not match "
    #                  "the numeric type and cannot be processed by the program\n")


def convert_expression_to_list(expression):
    """Converts str math expression into a list"""

    expression_list = expression.split(" ")
    return expression_list


def convert_list_element_to_number(expression_list):
    """Converts final result back to the number"""

    return expression_list[0]


def list_index_processor(expression_list, index_counter):
    """Process list elements that was already used for calculation
    into False values without immediately deleting them
    in order to prevent index inconsistencies"""

    expression_list[index_counter - 1] = False
    expression_list[index_counter] = False
    return expression_list


def exponentiation(expression_list):
    """Function that process exponentiation opeartion"""

    index_counter = 0

    for element in expression_list:

        if element == "**":
            result = int(expression_list[index_counter - 1]) ** int(expression_list[index_counter + 1])
            expression_list[index_counter - 1] = result
            del expression_list[index_counter]
            del expression_list[index_counter]

        index_counter += 1

    while False in expression_list:
        expression_list.remove(False)

    return expression_list


def multiplication_division(expression_list):
    """Function that process multiplication
     and division opeartions"""

    index_counter = 0

    for element in expression_list:

        if element == "*":
            expression_list[index_counter + 1] = (
                    int(expression_list[index_counter - 1]) *
                    int(expression_list[index_counter + 1]))
            list_index_processor(expression_list, index_counter)
        elif element == "/":
            expression_list[index_counter + 1] = (
                    int(expression_list[index_counter - 1]) /
                    int(expression_list[index_counter + 1]))
            list_index_processor(expression_list, index_counter)

        index_counter += 1

    while False in expression_list:
        expression_list.remove(False)

    return expression_list


def addition_subtraction(expression_list):
    """Function that process addition
     and subtraction opeartions"""

    index_counter = 0

    for element in expression_list:

        if element == "+":
            result = int(expression_list[index_counter - 1]) + int(expression_list[index_counter + 1])
            expression_list[index_counter + 1] = result
            list_index_processor(expression_list, index_counter)

        if element == "-":
            expression_list[index_counter + 1] = (
                    int(expression_list[index_counter - 1]) -
                    int(expression_list[index_counter + 1]))
            list_index_processor(expression_list, index_counter)

        index_counter += 1

    while False in expression_list:
        expression_list.remove(False)

    return expression_list


# assert calculator_engine("1 + 5 - 3") == 3
# assert calculator_engine("-33 + 1 * 2 ** 4 / 2 + 5 - 3 + 2 ** 2") == -19
b = "ee"
print(calculator_engine(""))

# "10 + n" ValueError: invalid literal for int() with base 10: 'n'
# "10 / 0" ZeroDivisionError: division by zero
# "10 - - " ValueError: invalid literal for int() with base 10: '-'
# "10 +" IndexError: list index out of range
# 5 + "bb" TypeError: unsupported operand type(s) for +: 'int' and 'str'
#
#
#
#
#
#
# def calculator(math_expression):
#     """Accepts math expression and calculates it.
#     Returns result of the calculation
#     Can process most Errors and provide messages
#     with explanation of what could be the reason of the Error"""
#     try:
#         math_expression = math_expression.replace(" ", "")
#         result = eval(math_expression)
#         return result
#
#     except ZeroDivisionError:
#         cprint.fatal("Деление на ноль: "
#                      "В выражении применяется деление на ноль, "
#                      "что не является допустимым действием\n")
#
#     except NameError:
#         cprint.fatal("Ошибка в выражении: "
#                      "Убедитесь, что введенное выражение содержит "
#                      "только числа, связанные математическими операторами\n")
#
#     except SyntaxError:
#         cprint.fatal("Ошибка в выражении: "
#                      "Убедитесь, что введенное выражение содержит "
#                      "только числа, связанные математическими операторами\n")
#
#     except TypeError:
#         cprint.fatal("Неверный тип данных: "
#                      "Тип полученных данных не соответствует "
#                      "числовому и не может быть обработан программой\n")
#
#     return "Произошла ошибка, повторите ввод"
#
#
# # TEST CASES
# assert calculator("5 + 4 9") == 54
# assert calculator("10 - 3 + 1 8") == 25
# assert calculator("2 ** 3 - 1 7") == -9
#
# assert not calculator("2 ** 3 - 17") == 100
#
# print(calculator(input("Пожалуйста, введите математическое выражение, "
#                        "которое Вы хотите вычислить...")))
