"""Детский сад — штаны на лямках
В продолжение темы детского сада давайте и там что-нибудь автоматизируем.
За каждым ребёнком закреплён шкафчик и кровать. Номер шкафчика состоит из трёх цифр:

номер группы в саду;
номер кроватки закреплённой за ребёнком;
порядковый номер ребёнка в списке группы.
Воспитатель просит сделать программу, которая по имени ребенка и номеру его шкафчика формирует «красивую» 
карточку для личного дела.

Формат ввода
В первой строке записано имя ребенка.
Во второй строке записан номер шкафчика.

Формат вывода
Карточка в виде:

Группа №<номер группы>.  
<номер ребёнка в списке>. <имя ребенка>.  
Шкафчик: <номер шкафчика>.  
Кроватка: <номер кроватки>.
Пример 1

Ввод
Ванечка
832
Вывод
Группа №8.
2. Ванечка.
Шкафчик: 832.
Кроватка: 3.

Пример 2
Ввод
Машенька
141
Вывод
Группа №1.
1. Машенька.
Шкафчик: 141.
Кроватка: 4.
Ограничение памяти
64.0 Мб
"""
name = input()
n = int(input())
number = n % 10
crib = n // 10 % 10
group_number = n // 100
print(f"Группа №{group_number}.\n{number}. {name}.\nШкафчик: {n}.\nКроватка: {crib}.")