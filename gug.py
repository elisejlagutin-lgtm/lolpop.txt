import random

# Генерируем случайное число от 1 до 100
secret_number = random.randint(1, 100)
attempts = 0

print("Добро пожаловать в игру 'Угадай число'!")
print("Я загадал число от 1 до 100. Попробуй угадать его.")

while True:
    guess = int(input("Введите ваше предположение: "))
    attempts += 1

    if guess < secret_number:
        print("Загаданное число больше.")
    elif guess > secret_number:
        print("Загаданное число меньше.")
    else:
        print(f"Поздравляем! Вы угадали число {secret_number} за {attempts} попыток.")
        break