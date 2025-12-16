def total_salary(path):
    return 0

def load_data(filename: str) -> list[str]:
    with open(filename, "r") as file:
        return file.readlines()

def clean_data(temperature_data: list[str]) -> list[float]:
    return [float(temp.strip()) for temp in temperature_data if temp.strip()]

def calculate_statistics(temperatures: list[float]) -> dict:
    if not temperatures:
        return None

    min_temp = min(temperatures)
    max_temp = max(temperatures)
    avg_temp = sum(temperatures) / len(temperatures)
    median_temp = calculate_median(temperatures)

    return {
        "min": min_temp,
        "max": max_temp,
        "average": avg_temp,
        "median": median_temp,
    }

def calculate_median(temperatures: list[float]) -> float:
    temperatures.sort()
    n = len(temperatures)
    mid = n // 2
    if n % 2 == 0:
        return (temperatures[mid - 1] + temperatures[mid]) / 2
    else:
        return temperatures[mid]

from data import load_data, clean_data
from processing import calculate_statistics

def main():
    filename = "temperatures.txt"
    raw_data = load_data(filename)
    temperatures = clean_data(raw_data)
    stats = calculate_statistics(temperatures)

    if stats:
        print(f"Minimum Temperature: {stats['min']}°C")
        print(f"Maximum Temperature: {stats['max']}°C")
        print(f"Average Temperature: {stats['average']:.2f}°C")
        print(f"Median Temperature: {stats['median']:.2f}°C")
    else:
        print("No temperature data available.")

if __name__ == "__main__":
    main()




# Перше завдання
# У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.

# Наприклад:
# Alex Korp,3000
# Nikita Borisenko,2000
# Sitarama Raju,1000

# Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників.

# Вимоги до завдання:
#     Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
#     Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
#     Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
#     Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.

# Рекомендації для виконання:
#     Використовуйте менеджер контексту with для читання файлів.
#     Пам'ятайте про встановлення кодування при відкриті файлів
#     Для розділення даних у кожному рядку можна застосувати метод split(',').
#     Обрахуйте загальну суму заробітної плати, а потім розділіть її на кількість розробників, щоб отримати середню зарплату.
#     Опрацьовуйте можливі винятки при роботі з файлами, такі як відсутність файлу.

# Критерії оцінювання:
#     Функція повинна точно обчислювати загальну та середню суми.
#     Повинна бути обробка випадків, коли файл відсутній або пошкоджений.
#     Код має бути чистим, добре структурованим і зрозумілим.

# Приклад використання функції:
# total, average = total_salary("path/to/salary_file.txt")
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

# Очікуваний результат:
# Загальна сума заробітної плати: 6000, Середня заробітна плата: 2000
