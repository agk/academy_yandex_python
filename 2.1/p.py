"""Доставка
Продуктовый склад и магазин находятся на одной дороге города Н.
Склад находится на отметке A км, а магазин — B км. Средняя скорость автомобиля, доставляющего товары, C км/ч.
За какое время продукты попадают со склада в магазин?

Формат ввода
Три натуральных числа A, B и C, каждое на отдельной строке.

Формат вывода
Одно рациональное число с точностью до сотых.

Пример 1
Ввод
10
32
5
Вывод
4.40

Пример 2
Ввод
1
100
30
Вывод
3.30
"""
a = int(input())
b = int(input())
c = int(input())
d = b - a
print(f"{d/c:0<4}")