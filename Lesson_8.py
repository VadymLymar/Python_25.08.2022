
# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.

my_list = ['qwe', 'rty', 'uio', 'pas', 'dfg']
new_list = [word if index % 2 == 1 else word[::-1] for index, word in enumerate(my_list)]
print(new_list)


# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".

my_list = ["Андрей", "Олег", "Алексей", "Дмитрий", "Людмила", "Вадим"]
new_list = [name for name in my_list if name[0].lower() == "а"]
print(new_list)


# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.

my_list = ["абракадабра", "мемчик", "Абзац", "море", "бровь"]
new_list = [word for word in my_list if "а" in word.lower()]
print(new_list)


# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
persons = [ {"name": "Sam", "age": 10},
            {"name": "Jackky", "age": 47},
            {"name": "Polly", "age": 12},
            {"name": "Jack", "age": 10},
            {"name": "Piter", "age": 13},
            {"name": "Pan", "age": 47},
            {"name": "Mal", "age": 12},
            {"name": "Jackly", "age": 42},]

# а) Создать список и поместить туда имя самого молодого человека. Если возраст совпадает - поместить все имена самых молодых.

min_age = float('inf')
for person in persons:
    if person['age'] < min_age:
        min_age = person['age']
names_min_age = [p['name'] for p in persons if p['age'] == min_age]
print(names_min_age)

# б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.

max_len = len(person['name'])
for person in persons:
    if len(person['name']) > max_len:
        max_len = len(person['name'])
names_max_len = [p['name'] for p in persons if len(p['name']) == max_len]
print(names_max_len)

# в) Посчитать среднее количество лет всех людей из начального списка.

names_avg_age = [p['age'] for p in persons]
print(sum(names_avg_age)/len(names_avg_age))


# 5) Даны два словаря my_dict_1 и my_dict_2.

my_dict_1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
my_dict_2 = {'f':6, 'a':7, 'g':8, 'b':9, 'h':10}

# а) Создать список из ключей, которые есть в обоих словарях.

same_keys_of_dicts = list(my_dict_1.keys() & my_dict_2.keys())

# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.

unique_keys_of_the_my_dict_1 = list(my_dict_1.keys() - my_dict_2.keys())

# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.

new_dict = {key: value for key, value in my_dict_1.items() if key in unique_keys_of_the_my_dict_1}

# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

custom_dict = {key: my_dict_1[key] for key in unique_keys_of_the_my_dict_1}
for key in same_keys_of_dicts:
    custom_dict[key] = [my_dict_1[key], my_dict_2[key]]

print(unique_keys_of_the_my_dict_1)
print(same_keys_of_dicts)
print(new_dict)
print(custom_dict)