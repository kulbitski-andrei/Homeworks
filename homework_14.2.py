"""HOMEWORK 14.2
Welcome to the Community version of Expression Calculator.
It supports such operations as exponentiation, multiplication,
division, addition and subtraction. To unlock more operations
please consider purchasing Advanced or Pro version."""

from cprint import cprint


def calculator_engine(expression):
    """Main function of the app that calls all other functions
    and handles different types of errors.
    Do not forget to provide a mathematical expression!"""

    try:

        result = (convert_list_element_to_number(
            addition_subtraction(
                multiplication_division(
                    exponentiation(
                        element_checker(
                            convert_expression_to_list(
                                expression)))))))

        return result

    except ZeroDivisionError:
        cprint.fatal("Division by zero: \n"
                     "The expression uses division by zero, \n"
                     "which is not a valid operation\n")

    except ValueError:
        cprint.fatal("Error in the expression: \n"
                     "Make sure the entered expression contain \n"
                     "only numbers connected by mathematical operators. \n"
                     "All elements should be separated by a spaces\n")

    except SyntaxError:
        cprint.fatal("Error in the expression: \n"
                     "Make sure the entered expression contain \n"
                     "only numbers connected by mathematical operators. \n"
                     "All elements should be separated by a spaces\n")

    except IndexError:
        cprint.fatal("Error in the expression: \n"
                     "Make sure the entered expression contain \n"
                     "only numbers connected by mathematical operators. \n"
                     "All elements should be separated by a spaces\n")

    except TypeError:
        cprint.fatal("Incorrect data type: \n"
                     "The type of the received data does not match \n"
                     "the numeric type and cannot be processed "
                     "by the program.\n")

    return None


def convert_expression_to_list(expression):
    """Converts str math expression into a list"""

    expression_list = expression.split(" ")
    return expression_list


def element_checker(expression_list):
    """Raises Value error if one or more elements
    in provided expression are neither numeric
    nor mathematical operators"""

    for element in expression_list:
        if element[0] == "-" and element != "-":
            element = float(element)
        if (str(element).isdigit() or isinstance(element, float)
                or element in ['+', '-', '*', '/', '**']):
            pass
        else:
            raise ValueError
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
            result = (int(expression_list[index_counter - 1]) **
                      int(expression_list[index_counter + 1]))
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
            result = (int(expression_list[index_counter - 1]) +
                      int(expression_list[index_counter + 1]))
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


print(calculator_engine(input("~ ")))

# TEST CASES
assert calculator_engine("5 + 49") == 54
assert calculator_engine("10 - 3 + 18") == 25
assert calculator_engine("2 ** 3 - 17") == -9
assert calculator_engine("-33 + 1 * 2 ** 4 / 2 + 5 - 3 + 2 ** 2") == -19
