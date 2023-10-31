yesterday_temp = int(input())
today_temp = int(input())
if today_temp > yesterday_temp:
    print("Сегодня теплее, чем вчера.")
elif today_temp < yesterday_temp:
    print("Сегодня холоднее, чем вчера.")
else:
    print("Сегодня такая же температура, как вчера.")


print("Введите первую и последнюю буквы русского алфавита.")
first_letter = input()
last_letter = input()
if (first_letter == "а" or first_letter == "А") and (
        last_letter == "я" or last_letter == "Я"):
    print("Верно.")
else:
    print("Неверно.")


text = input()
if "добр" in text:
    print("Встретилось 'доброе' слово.")
else:
    print("Добрых слов не найдено.")



color = input()
match color:
    case 'красный' | 'жёлтый':
        print('Стоп.')
    case 'зелёный':
        print('Можно ехать.')
    case _:
        print('Некорректное значение.')


m = 12
n = 19
k = 25
# максимальное число
print(max(m, n, k))

line_1 = "m"
line_2 = "n"
line_3 = "k"
# минимальная лексикографически строка
print(min(line_1, line_2, line_3))

# количество цифр в числе 2 в степени 2022
print(len(str(2 ** 2022)))

