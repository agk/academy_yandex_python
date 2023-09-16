"""Дед Мороз и конфеты
Настало самое главное событие в детском саду — новогодний утренник.
Хорошо замаскированная робоняня в роли Деда Мороза решила раздать детям конфеты так, чтобы каждому досталось поровну. Напишите для робоняни алгоритм, который поможет распределить конфеты.

Формат ввода
В первой строке указано количество детей на утреннике.
Во второй строке — количество конфет в конфетном отсеке робоняни.

Формат вывода
Сначала выведите количество конфет, которое выдано каждому ребенку, а затем количество конфет, что осталось в конфетном отсеке.

Пример 1
Ввод
3
100
Вывод
33
1
Пример 2
Ввод
20
500
Вывод
25
0
Ограничение памяти
64.0 Мб
Ограничение времени
1 с
Ввод
стандартный ввод или input.txt
Вывод
стандартный вывод или output.txt"""
children = int(input())
candies = int(input())
print(int(candies / children), (candies % children), sep="\n") 