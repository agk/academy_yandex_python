"""Делу — время, потехе — час
Давайте передохнём от автоматизации и сделаем что-то действительно интересное.

Формат ввода
Одно натуральное число N

Формат вывода
N строк с фразой: "Купи слона!"

Пример 1
Ввод
1
Вывод
Купи слона!

Пример 2
Ввод
3
Вывод
Купи слона!
Купи слона!
Купи слона!
"""
str = "Купи слона!"
n = int(input())
print(f"{str}\n" * (n - 1) + str)