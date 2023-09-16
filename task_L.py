"""Интересное сложение
Один малыш из детского сада услышал от старшей сестры о некоем действии с числами — сложении.
И как это часто бывает — он не до конца разобрался, как работает сложение. Например, не совсем понял, как произвести перенос разряда.
Теперь он хочет научить сложению остальных ребят и просит написать программу, которая поможет ему в качестве наглядного материала.

Формат ввода
В первой и второй строках записаны натуральные числа меньше 1000.

Формат вывода
Одно число — результат сложения введённых чисел без учёта переносов.

Пример 1
Ввод
123
99
Вывод
112
Пример 2
Ввод
405
839
Вывод
234
Ограничение памяти
64.0 Мб
Ограничение времени
1 с
Ввод
стандартный ввод или input.txt
Вывод
стандартный вывод или output.txt"""
n = int(input())
m = int(input())

nc = n % 10
nb = n // 10 % 10
na = n // 100 % 10

mc = m % 10
mb = m // 10 % 10
ma = m // 100 % 10

rc = (nc + mc) % 10
rb = (nb + mb) % 10
ra = (na + ma) % 10

print(ra, rb, rc, sep = "") 