# 1) У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.

my_list = []
for number in range(90, 110):
    if number > 100:
        my_list.append(number)
print(my_list)
######################################

# 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.

my_list = []
my_results = []
for number in range(90, 110):
    if number > 100:
        my_results.append(number)
    else:
        my_list.append(number)
print(my_results)
print(my_list)
######################################

# 3) У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)

my_list = [1, 2, 3, 50]
if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-2]+my_list[-1])
print(my_list)