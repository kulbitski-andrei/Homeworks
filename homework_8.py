# 1. Последовательность¶
# Дана последовательность целых чисел в виде массива.
# Определите, можно ли получить строго возрастающую последовательность,
# удалив из массива не более одного элемента.
# Примечание: последовательность a0, a1, ..., an считается строго возрастающей,
# если a0 < a1 < ... < an.
# Последовательность, содержащая только один элемент, также считается строго возрастающей.
# Примеры
# Для последовательности = [1, 3, 2, 1], вывод должен быть решение = False.
# В этом массиве нет ни одного элемента, который можно было бы удалить,
# чтобы получить строго возрастающую последовательность.
# Для последовательности = [1, 3, 2] вывод должен быть = True.
# Вы можете удалить 3 из массива, чтобы получить строго возрастающую последовательность [1, 2].
# Альтернативно можно убрать 2, чтобы получить строго возрастающую последовательность [1, 3].
# solution([1, 2, 3])
# solution([1, 2, 1, 2])
# solution([1, 3, 2, 1])
# solution([1, 2, 3, 4, 5, 3, 5, 6])
# solution([40, 50, 60, 10, 20, 30])



# 2. Число напротив¶

def numeric_circle(n, first_number):

    distance = n / 2  # Distance on the scale from first number to second number
    # print("Distance:", distance)

    if first_number >= distance:
        second_number = first_number - distance
    else:
        second_number = first_number + distance

    return int(second_number)


print(numeric_circle(30, 2))


# 3. Валидировать номер кредитной карты через алгоритм Луна

def validate(credit_card_input):

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
    else:
        return True


# print(validate(4561261212345464))  # False expected
# print(validate(4561261212345467))  # True expected
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
