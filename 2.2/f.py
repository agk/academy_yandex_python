"""
Сила прокрастинации
Вася любит полениться. Особенно ему нравится, когда в году появляется такой лишний денёк, которого обычно не бывает. 
Напишите программу, которая поможет Васе определить, удастся ли ему побездельничать в определённом году или нет.

Формат ввода
Одно число — год.

Формат вывода
Одно слово «YES» (удастся) или «NO» (не удастся).

Пример 1

Ввод
2022
Вывод
NO
Пример 2

Ввод
2020
Вывод
YES
"""
y = int(input())
print('YES') if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) else print('NO') 