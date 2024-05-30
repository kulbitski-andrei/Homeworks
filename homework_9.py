# """HOMEWORK #9"""

# 1. Строки с заданным символом¶


def text_filter(text):
    """Accepts string, returns filtered string,
    removing every '#' character and one character before it"""

    text_list = list(text)
    text_filtered = ""

    while "#" in text_list:

        character_index = 0

        for i in text_list:
            if i == "#":
                text_list.pop(character_index)
                if character_index - 1 >= 0:
                    text_list.pop(character_index - 1)
                break

            character_index += 1

    for element in text_list:
        text_filtered += element

    return text_filtered


# TEST CASES
print("\nTask 1")
print(text_filter("abc#d##c"))

pass
pass
pass
pass


# 3. Подсчет количества букв¶

def char_counter(text):
    """Accepts string, returns string
    with calculation of amount of every character"""
    text_improved = ""
    used_chars = []

    for char_letter in text:
        if char_letter not in used_chars:
            used_chars.append(char_letter)
            counter = text.count(char_letter)
            if counter == 1:
                counter = ""
            text_improved += f"{char_letter}{counter}"

    return text_improved


# TEST CASES
print("\nTask 3")
print(char_counter("cccbba"))
print(char_counter("abeehhhhhccced"))
print(char_counter("aaabbceedd"))
print(char_counter("abcde"))
print(char_counter("aaabbdefffff"))
