# 1. Дано целое число(int).Определить сколько нулей в этом числе.

# my_number = 150000
# numders_zero = str(my_number).count("0")
# print(numders_zero)


# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля
# my_number = 1002000
# str_number = str(my_number)
# numders_zero_end = len(str_number) - len(str(int(str_number[::-1])))
# print(numders_zero_end)


# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

# my_list_1 = [1, 2, 3, 4, 5, 6, 7]
# my_list_2 = [10, 20, 30, 40]
# my_result = []
# for numbers in my_list_1[::2]:
#     my_result.append(numbers)
# my_result += list(my_list_2[1::2])
# print(my_result)


# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]

# my_list = [1, 2, 3, 4]
# new_list = my_list[1:] + [my_list[0]]
# print(new_list)


# 5. Дано список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

# my_list = [1, 2, 3, 4]
# my_list += [my_list.pop(0)]
# print(my_list)


# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)

# str = "43 больше чем 34 но меньше чем 56"
# arr = str.split()
# sum_number = sum([int(i) for i in arr if i.isdigit()])
# print(sum_number)


# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin". (rfind, find - методы строк)

# my_str = "My long string"
# l_limit, r_limit = "o", "g"
# sub_str = my_str[my_str.find(l_limit) + 1:my_str.rfind(r_limit)]
# print(sub_str)


# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)

# my_str = "My long string"
# if len(my_str) % 2 != 0:
#     my_str += "_"
# lst = [my_str[i] + my_str[i+1] for i in range(0, len(my_str)-1, 2)]
# print(lst)


# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

# my_list = [2, 4, 1, 5, 3, 9, 0, 7]
# counter = 0
# for index in range(1, len(my_list) - 1):
#     if my_list[index] > sum([my_list[index - 1], my_list[index + 1]]):
#         counter += 1
# print(counter)


# 10. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.

# my_list = [1, 2, 3, "11", "22", 33]
# new_list = [item for item in my_list if type(item) == str]
# print(new_list)


# 11. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз.

# my_str = 'Любая строка'
# lst = [char for char in set(my_str) if my_str.count(char) == 1]
# print(lst)


# 12. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

# my_str_1 = 'Hi! Nice to meet you!'
# my_str_2 = 'Hi! Nice to meet you!'
# my_lst = list(set(my_str_1).intersection(set(my_str_2)))
# my_lst = [char for char in set(my_str_1) if char in my_str_2]
# print(my_lst)


# 13. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу.
# Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"], т.к. эти символы есть в каждой строке по одному разу

# my_str_1 = 'aaaasdf1'
# my_str_2 = 'asdfff2'
# new_lst = [char for char in set(my_str_1) if my_str_1.count(char) == my_str_2.count(char) == 1]
# print(new_lst)