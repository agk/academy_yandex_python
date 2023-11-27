"""В ожидании доставки
Сегодня в N часов M минут хозяин магазина заказал доставку нового товара. 
Оператор сказал, что продукты доставят через T минут.
Сколько будет времени на электронных часах, когда привезут долгожданные продукты?

Формат ввода
В первой строке записано натуральное число N (0≤N<24).
Во второй строке записано натуральное число M (0≤M<60).
В третьей строке записано натуральное число T (30≤T<10 9).

Формат вывода
Одна строка, представляющая циферблат электронных часов.

Пример 1
Ввод
8
0
65
Вывод
09:05

Пример 2
Ввод
10
15
2752
Вывод
08:07
"""
n = int(input())
m = int(input())
t = int(input())
time_min = n * 60 + m + t
hour, min = int(time_min / 60) % 24, time_min % 60

print(f"{hour:0>2}:{min:0>2}")