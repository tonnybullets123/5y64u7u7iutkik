# Функция для подсчета слов
def count_words(text):
    words = text.split()
    return len(words)

# Основная программа
def main():
    print("Подсчет слов в тексте")
    text = input("Введите текст: ")
    if text.strip():
        word_count = count_words(text)
        print(f"Количество слов: {word_count}")
    else:
        print("Текст пустой!")

if __name__ == "__main__":
    main()