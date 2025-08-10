# Функция для проверки, является ли число простым
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Основная программа
def main():
    print("Проверка простого числа")
    try:
        number = int(input("Введите число: "))
        if is_prime(number):
            print(f"{number} - простое число")
        else:
            print(f"{number} - не простое число")
    except ValueError:
        print("Введите целое число!")

if __name__ == "__main__":
    main()