"""Сдача 10
Кстати, несмотря на ошибку аппарата, сдачу тоже нужно отдавать.

Формат ввода
Цена покупки — двоичное число, выданное кассовым аппаратом.
Номинал купюры пользователя — десятичное число (≥100≥100).

Формат вывода
Одно десятичное число — сдача, которую требуется отдать пользователю.

Примечание
Все числа, используемые в задаче, целые.

Пример 1

Ввод
1001001
100
Вывод
27
Пример 2

Ввод
101111100
500
Вывод
120
Ограничение памяти
64.0 Мб
Ограничение времени
1 с
Ввод
стандартный ввод или input.txt
Вывод
стандартный вывод или output.txt"""
price = input()
banknote = int(input())
print(banknote - int(price, 2))