import random

print("Выберите уровень сложности:")
print("1. Легкий")
print("2. Средний")
print("3. Сложный")
try:
    difficulty = int(input("Введите номер сложности (1, 2 или 3): "))
    
    if difficulty in [1, 2, 3]:
    print("Число верное")
else:
    print("Число неверное")

except ValueError:
    print("Ошибка: Введите целое число (1, 2 или 3).")

if difficulty == 1:
    number_range = 10
elif difficulty == 2:
    number_range = 20
else:
    number_range = 50

num1 = random.randint(1, number_range)
num2 = random.randint(1, number_range)

operator = random.choice(['+', '-', '*', '/'])

question = f"{num1} {operator} {num2}"

if operator == '+':
    correct_answer = num1 + num2
elif operator == '-':
    correct_answer = num1 - num2
elif operator == '*':
    correct_answer = num1 * num2
elif operator == '/':
    while num2 == 0:
        num2 = random.randint(1, number_range)
    correct_answer = num1 / num2

print(f"Вопрос: {question}")

user_answer = input("Ваш ответ: ")

if float(user_answer) == correct_answer:
    print("Правильно!")
else:
    print(f"Неправильно. Правильный ответ: {correct_answer}")
