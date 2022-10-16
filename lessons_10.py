# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).

# file_name = "Homework/domains.txt"
#
# def get_domains(file_name: str) -> list:
#     with open(file_name, "r") as domains:
#         domains = [domain.strip(".\n") for domain in domains.readlines()]
#     return domains
#
# Test_For_Domains = get_domains(file_name)
# print(Test_For_Domains)

# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# # Разделитель - символ табуляции "\t"

# file_name = "Homework/names.txt"
#
# def get_surnames(file_name: str) -> list:
#     with open(file_name, "r") as names:
#         surnames = [line_info.split()[1] for line_info in names.readlines()]
#     return surnames
#
# Test_For_Surnames = get_surnames(file_name)
# print(Test_For_Surnames)


# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date": date}
# в которых date - это дата из строки (если есть),
# Например [{"date": "1st January 1919"}, {"date": "8th February 1828"},  ...]
# file_name = "Homework/authors.txt"
#
# def get_dates(file_name: str) -> list:
#     dates = []
#     with open(file_name, "r") as file:
#         for line in file.readlines():
#             if "-" in line:
#                 dates += [{"date":line.split("-")[0].strip()}]
#     return dates
#
# Test_For_Authors = get_dates(file_name)
# print(Test_For_Authors)


# По просьбам некоторых студентов начну включать дополнительные задания.
# 4* (*сдавать не обязательно, но если будете сдавать, то ошибки будут учитываться тоже).
# Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date_original": date_original, "date_modified": date_modified}
# в которых date_original - это дата из строки (если есть),
# а date_modified - это та же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]
