"""Автоматизация игры
Всё в том же детском саду ребята очень любят играть с цифрами.
Одна из таких игр — перестановка цифр четырёхзначного числа.
Напишите программу для робота-няни, которая из числа вида abcd составляет число badc.

Формат ввода
Одно четырёхзначное число.

Формат вывода
Одно четырёхзначное число — результат перестановки.

Пример 1
Ввод
1234
Вывод
2143

Пример 2
Ввод
1412
Вывод
4121
"""
n = int(input())
d = n % 10
c = n // 10 % 10
b = n // 100 % 10
a = n // 1000 % 10
print(b, a, d, c, sep="")