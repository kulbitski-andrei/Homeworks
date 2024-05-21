"""HOMEWORK #6"""

# 1. Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
sample_string_1 = "Robin Singh"
sample_list_1 = sample_string_1.split()
print(sample_list_1)


# 2. Перевести строку в список
# "I love arrays they are my favorite" =>
# ["I", "love", "arrays", "they", "are", "my", "favorite"]
sample_string_2 = "I love arrays they are my favorite"
sample_list_2 = sample_string_2.split(" ")
print(sample_list_2)


# 3. Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
name_list = ["Ivan", "Ivanou"]
name_str = " ".join(name_list)
city_str = "Minsk"
country_str = "Belarus"
print(f"Привет, {name_str}! Добро пожаловать в {city_str} {country_str}")


# 4. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"
sample_list_3 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
sample_string_3 = " ".join(sample_list_3)
print(sample_string_3)


# 5. Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
sample_list_4 = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
print(sample_list_4)
sample_list_4.insert(2, 777)
sample_list_4.pop(6)
print(sample_list_4)
