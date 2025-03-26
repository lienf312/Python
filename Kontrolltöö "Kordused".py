#вывод n елoк

n = int(input("Введите число n (от 1 до 9): "))
tree = [
    " /V\\    ",
    " / V \\   ",
    " / V V \\  ",
    "/VV V VV\\ "
]

for i in range(4):
    for j in range(n):
        print(tree[i], end=" ")
    print()


#Перемножить все нечётные значения в диапазоне от 0 до R

R = int(input("Введите число R: "))
product = 1
for i in range(1, R + 1, 2):
    product *= i
print("Результат перемножения нечётных чисел:", product)


#Найти количество положительных чисел среди N случайных чисел

import random

N = random.randint(5, 10)  # случайное количество чисел
positive_count = 0

for _ in range(N):
    number = random.randint(-10, 10)
    if number > 0:
        positive_count += 1

print("Количество положительных чисел:", positive_count)


#Посчитать чётные и нечётные цифры числа

num = int(input("Введите число: "))
even_count = 0
odd_count = 0

while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    num //= 10

print(f"Чётные цифры: {even_count}, Нечётные цифры: {odd_count}")


#Найти сумму ряда чисел от A до B

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
sum_series = sum(range(A, B + 1))
print("Сумма ряда чисел:", sum_series)
