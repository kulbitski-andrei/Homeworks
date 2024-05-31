"""HOMEWORK #9"""


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
assert text_filter("a#bc#d") == "bd"
assert text_filter("abc#d##c") == "ac"
assert text_filter("abc##d######") == ""
assert text_filter("#######") == ""
assert text_filter("") == ""


# 2. Свечи

def candle_counter(candle_number, make_new):
    """Accepts start amount of candles (candle_number) and
    amount of candle stubs needed to create a new candle (make_new).
    Returns total amount of candles user can burn"""

    ogarochki = 0
    total_candles_burnt = 0

    while candle_number > 0:
        total_candles_burnt += candle_number
        ogarochki += candle_number
        candle_number = ogarochki // make_new
        ogarochki = ogarochki % make_new

    return total_candles_burnt


# TEST CASES
assert candle_counter(5, 2) == 9
assert candle_counter(1, 2) == 1
assert candle_counter(15, 5) == 18
assert candle_counter(12, 2) == 23
assert candle_counter(6, 4) == 7
assert candle_counter(13, 5) == 16
assert candle_counter(2, 3) == 2


# 3. Подсчет количества букв¶

def char_counter(text):
    """Accepts string, returns string
    with calculation of amount of every character"""
    text_improved = ""
    counter = 0
    new_letter = True
    position_index = -1

    # for _ in range(len(text)):
    for _ in text:

        position_index += 1

        if position_index == len(text) - 1:
            if counter < 2:
                counter = ""
            text_improved += f"{text[position_index]}{counter}"
            return text_improved

        if new_letter:
            counter += 1
            new_letter = False

        if text[position_index] != text[position_index + 1]:
            if counter < 2:
                counter = ""
            text_improved += f"{text[position_index]}{counter}"
            new_letter = True
            counter = 0
        else:
            counter += 1

    return None


# TEST CASES
assert char_counter("cccbba") == "c3b2a"
assert char_counter("abeehhhhhccced") == "abe2h5c3ed"
assert char_counter("aaabbceedd") == "a3b2ce2d2"
assert char_counter("abcde") == "abcde"
assert char_counter("aaabbdefffff") == "a3b2def5"
