"""Сдача
Чаще всего автоматизация идёт на пользу.
Одна из задач, в которой лучше исключить человеческий фактор, — подсчёт сдачи.
Определите, какую сдачу нужно выдать тому, кто купил 2,5кг черешни по цене 38 руб/кг.

Формат ввода
Одно натуральное число - номинал купюры пользователя (≥100≥100).

Формат вывода
Одно натуральное число — размер сдачи.

Пример

Ввод
100
Вывод
5
"""
k = int(input())
sum = int(2.5 * 38)
print(k - sum)