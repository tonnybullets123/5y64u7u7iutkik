# Функция для вывода таблицы умножения
def multiplication_table(n):
    print(f"Таблица умножения для {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Основная программа
def main():
    try:
        num = int(input("Введите число для таблицы умножения (1-10): "))
        if 1 <= num <= 10:
            multiplication_table(num)
        else:
            print("Число должно быть от 1 до 10!")
    except ValueError:
        print("Введите целое число!")

if __name__ == "__main__":
    main()