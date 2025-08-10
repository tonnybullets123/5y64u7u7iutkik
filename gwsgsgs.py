# Функция для вычисления факториала
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Основная программа
def main():
    print("Калькулятор факториала")
    try:
        num = int(input("Введите число (0-20): "))
        if 0 <= num <= 20:
            result = factorial(num)
            print(f"Факториал {num}! = {result}")
        else:
            print("Число должно быть от 0 до 20!")
    except ValueError:
        print("Введите целое число!")

if __name__ == "__main__":
    main()