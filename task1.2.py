import random

def get_numbers_ticket(min_val, max_val, quantity):
    """
    Генерує набір унікальних випадкових чисел для лотерейного квитка.

    :param min_val: int, мінімальне можливе число у наборі (не менше 1).
    :param max_val: int, максимальне можливе число у наборі (не більше 1000).
    :param quantity: int, кількість чисел, які потрібно вибрати.
    :return: list, відсортований список унікальних випадкових чисел, або пустий список для некоректних параметрів.
    """
    # Перевірка 
    if not (1 <= min_val <= max_val <= 1000):
        return []
    if not (1 <= quantity <= (max_val - min_val + 1)):
        return []
    
    # Генерація унікальних випадкових чисел
    numbers = random.sample(range(min_val, max_val + 1), quantity)
    # Сортування 
    return sorted(numbers)

# Приклади 
if __name__ == "__main__":
    print(get_numbers_ticket(1, 49, 6))  # Наприклад: [3, 15, 23, 34, 45, 49]
    print(get_numbers_ticket(10, 20, 5))  # Наприклад: [10, 12, 15, 18, 20]
    print(get_numbers_ticket(1, 1000, 0))  # Некоректні параметри: []
    print(get_numbers_ticket(50, 49, 6))  # Некоректні параметри: []