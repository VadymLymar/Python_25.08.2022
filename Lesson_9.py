






# Для задания 1-7 за основу можете взять код из предідущих ДЗ.
#
# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.

# def reverse_list(list):
#     return [word if index % 2 == 1 else word[::-1] for index, word in enumerate(list)]
#
# my_list = ['qwe', 'rty', 'uio', 'pas', 'dfg']
# new_list: list = reverse_list(my_list)
# new_list.sort()
# print(new_list)


# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".

# def filter_list(list):
#     return [word for word in list if word[0].lower() == "a"]
#
# my_list = ['Apple', 'Mango', 'apricot', 'kiwifruit', 'grape', 'avocado']
# new_list = filter_list(my_list)
# new_list.sort()
# print(new_list)


# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.

# def filter_word(list):
#     return [word for word in list if "a" in word.lower()]
#
# my_list = ['Apple', 'Mango', 'apricot', 'kiwifruit', 'grape', 'avocado']
# new_list = filter_word(my_list)
# new_list.sort()
# print(new_list)

# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.

# def filter_item(list):
#     return [item for item in list if type(item) == str]
#
# my_list = ['Apple', 1, 'Mango', 2, 'apricot', 3, 'kiwifruit', 4]
# new_list = filter_item (my_list)
# new_list.sort()
# print(new_list)


# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.

# def return_list(str):
#     return [i for i in set(str) if str.count(i) == 1]
#
# my_str = 'Любая строка'
# lst = return_list (my_str)
# lst.sort()
# print(lst)

# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках хотя бы раз.

# def repeat_symbol(first_str: str, second_str: str):
#     return [symbol for symbol in set(first_str) if symbol in second_str]
#
# my_str_1 = "Любая строка на сегодня."
# my_str_2 = "Любая строка на завтра."
# new_str = repeat_symbol(my_str_1, my_str_2)
# new_str.sort()
# print(new_str)


# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

# def repeat_symbol(first_str: str, second_str: str):
#     return [symbol for symbol in set(first_str) if first_str.count(symbol) == second_str.count(symbol) == 1]
#
# my_str_1 = "Любая строка на сегодня."
# my_str_2 = "Любая строка на завтра."
# new_str = repeat_symbol(my_str_1, my_str_2)
# print(new_str)


# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.

#
# Пример использования функции:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com

import random
import string

surnames = ["smith", "martinez", "hernandez", "rodriguez", "lopes", "johnson", "williams", "brown", "jones", "miller"]
domains = ["com", "net", "us", "ua", "me", "org", "gov"]

def generate_email(surnames: list = surnames, domains: list = domains) -> str:
    random_surname = random.choice(surnames)
    random_number = random.randint(100, 999)
    length_of_the_random_string = random.randint(5, 7)
    random_string = "".join([random.choice(string.ascii_lowercase) for _ in range(length_of_the_random_string)])
    random_domain = random.choice(domains)
    return f"{random_surname}.{random_number}@{random_string}.{random_domain}"

e_mail = generate_email(surnames, domains)
print(e_mail)
