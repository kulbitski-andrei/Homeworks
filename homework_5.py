"""HOMEWORK #5"""
# 1. Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
# 2. Напишите программу, которая добавляет ‘ing’ к словам
# 3. В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
# 4. Напишите программу которая удаляет пробел в начале, в конце строки
# 5. Имена собственные всегда начинаются с заглавной буквы,
# за которой следуют строчные буквы.
# Исправьте данное имя собственное так,
# чтобы оно соответствовало этому утверждению:
# "pARiS" >> "Paris"

# 1. Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
sample_str = "www.my_site.com#about"
sample_str = sample_str.replace("#", "/")
print(sample_str)

# 2. Напишите программу, которая добавляет ‘ing’ к словам
user_input = input("Введите текст...")
improved_text = user_input + "ing"
print(improved_text)

# 3. В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
text_var = "Ivanou Ivan"
print("Было: ", text_var)
list_var = text_var.split()
# print(list_var)
list_var.reverse()
print("Стало: ", end=" ")
for i in list_var:
    print(i + " ", end="")
print("")

# 4. Напишите программу которая удаляет пробел в начале, в конце строки
text_string = input("Введите текст. Пробелы слева и справа будут удалены.")
strip_string = text_string.strip()
print(strip_string)

# 5. Имена собственные всегда начинаются с заглавной буквы,
# за которой следуют строчные буквы.
# Исправьте данное имя собственное так,
# чтобы оно соответствовало этому утверждению: "pARiS" >> "Paris"
paris_text = "pARiS"
paris_text_low = paris_text.lower()
# print(paris_text_low)
paris_text_up = paris_text_low[0].upper() + paris_text_low[1:]
print(paris_text_up)
