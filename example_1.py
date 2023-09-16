phrase = input("Введите строку: ")
print(phrase)

name = "Пользователь"
print(f"Добрый день {name}.")

print(f"{123:0>9}")
print(f"{123:0<9}")
print(f"{123:0^9}")

n_1 = "1"
n_2 = "2"
print(n_1 + n_2)
n_1 = int(n_1)
n_2 = int(n_2)
print(n_1 + n_2)

width = "3.7"
height = "2.5"
s = float(width) * float(height)
print(s)


n = 25
x = 0.5
print(n + x)
print(n - x)
print(n * x)
print(n / x)
print(n ** x)


print(f"{2 ** 0.5:.2f}")

last_digit = 1234 % 10
penultimate_digit = 1234 // 10 % 10

