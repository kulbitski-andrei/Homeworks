""""HOMEWORK #7. Andrei Kulbitski"""

import random

# 1. Быки и коровы¶
print("TASK 1: BULLS AND COWS")


def magic_number_generator_func():
    """Random unique 4-digit generator"""
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    random.shuffle(digits)
    return digits[:4]


# Magic number is stored as four integers packaged in the list
magic_number = magic_number_generator_func()

# User is expected to guess the number in four attempts :)
print(magic_number)
attempts = 8

while True:

    # Position counter for simultaneous enumeration of two lists
    position_key = 0
    # Bulls - amount of full alignments (digit and position)
    count_of_bulls = 0
    # Cows - amount of partial alignments (digit only)
    count_of_cows = 0

    while True:
        # Handling user input:
        # Every non-4-digit input will be rejected
        # and user would be forced to retry
        current_attempt = input(
            "Try to guess the magical number. Enter four digits: ... ")
        if current_attempt.isdigit() and len(current_attempt) == 4:
            current_attempt_list = []
            for i in current_attempt:
                # User input is stored as four integers packaged in the list
                current_attempt_list.append(int(i))
            break

        print("Wrong input: 4 digits expected. "
              "Please, follow the next pattern: XXXX.")

    for digit_b in magic_number:
        # Loop for calculation of amount of bulls
        if digit_b == current_attempt_list[position_key]:
            count_of_bulls += 1
        position_key += 1
    print("Bulls:", count_of_bulls)

    for digit_c in magic_number:
        # Loop for calculation of amount of cows
        if digit_c in current_attempt_list:
            count_of_cows += 1
    print("Cows:", count_of_cows)

    if count_of_bulls == 4:
        # Victory condition is met
        print("Congratulations, you have won!")
        break

    attempts -= 1

    if attempts <= 0:
        # Victory condition is not met
        print(f"You have no attempts left. "
              f"Game over. The magic number was {magic_number}")
        break

    print(f'{attempts} attempts left!')

# 2. Пирамида¶
print("\nTASK 2: PYRAMID")

var_N = int(input("Please enter pyramid size... "))
starfield = 1

while var_N != 0:
    print(" " * var_N, end="")
    print("*" * starfield)

    var_N -= 1
    starfield += 2

# 3. Статуи¶
print("\nTASK 3: STATUESQUES")


def birthday_presents_sorted_func(*args):
    """Returns birthday presents as a sorted list of statuesques"""
    birthday_presents = list(args)
    birthday_presents.sort()
    return birthday_presents


statuesques = birthday_presents_sorted_func(2, 15, 8, 4, 7, 12, 3, 16, 10, 5)
print(statuesques)

smaller_statuesque_size = min(statuesques)
print("The smaller statuesque is:", smaller_statuesque_size)

larger_statuesque_size = max(statuesques)
print("The larger statuesque is:", larger_statuesque_size)

min_max_gap = larger_statuesque_size - smaller_statuesque_size - 1
print(f"There are {min_max_gap} statuesques expected "
      f"to be in range between the larger one and smaller one...")

medium_size_quantity = len(statuesques) - 2
if medium_size_quantity != min_max_gap:
    print(f"But you only have {medium_size_quantity} of them!")
    print(f"You are missing {min_max_gap - medium_size_quantity} pieces!")
    print("You need to wait for the next birthday "
          "to receive more statuesques as a presents!")
else:
    print("You have as many statuesques as you need. Perfection!")
