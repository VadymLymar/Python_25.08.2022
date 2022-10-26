

import json
import re

file = "data.json"


#data.json - файл с данными о некоторых математиках прошлого.
# 1. Условие: Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.

def read_json(filename: str = file) -> dict:
    with open(filename, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


# 2. Написать "функцию сортировки" данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.

def sort_by_surname(item: dict) -> str:
    surname = item["name"].split()[-1]
    return surname


sorted_by_surnames = sorted(read_json(), key=sort_by_surname)
print(sorted_by_surnames)

# 3. Написать функцию сортировки по количеству слов в поле "text".


def sort_by_count_of_words(item: dict) -> tuple:
    text = item["text"]
    text_words = text.split()
    return len(text_words), text


sorted_by_count_of_words = sorted(read_json(), key=sort_by_count_of_words)
print(sorted_by_count_of_words)

# 4. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.


def sort_by_year(item: dict) -> int:
    years_of_life = item["years"]
    is_BC = True if re.findall(r"BC", years_of_life) != [] else False
    year_of_death = "".join(re.findall(r"[0-9]", years_of_life.split("–")[1]))
    if is_BC:
        year_of_death = f"-{year_of_death}"
    return int(year_of_death)


sorted_by_year = sorted(read_json(), key=sort_by_year)
print(sorted_by_year)
# Кроме функций сортировки также надо написать их использование.
