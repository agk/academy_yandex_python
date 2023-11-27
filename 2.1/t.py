"""Мухи отдельно, котлеты отдельно
Вернёмся в магазин, хозяин которого уже привык полагаться на всемогущую автоматизацию.

Помогите ему разобраться с одной проблемой. Далее его история: «Пару дней назад я купил две партии котлет 
и по случайности высыпал их на один прилавок. 
Общий вес котлет составил N килограмм, а ценник — M рублей за килограмм.
Сегодня я обнаружил, что накладные на эти виды котлет потерялись, но я помню, 
что первый вид котлет стоил K1 рублей за килограмм, а второй — K2.

Помогите мне вспомнить вес каждой партии котлет, чтобы поставить их на учёт.
Формат ввода
В первой строке записано натуральное число N
Во второй строке — натуральное число M
В третьей строке — натуральное число K1
В четвёртой строке — натуральное число K2

Причём доподлинно известно, что второй вид котлет стоит меньше, чем первый.
Формат вывода
Два натуральных числа, записанных через пробел — вес обеих партий котлет.

Пример
Ввод
32
285
300
240
Вывод
24 8
"""
n, m = int(input()), int(input())
k1, k2 = int(input()), int(input())
# x + y = N
# K1 * x + K2 * y = M * N
for x in range(1, n):
    # for y in range(1, n):
    #    if x > y and x * k1 + y * k2 == n * m:
    #        print(x, y)
    if (k1 - k2) * x == (m - k2) * n:
        print(x, n - x)