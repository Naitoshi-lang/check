#Рекурсивная сумма нечетных чисел

def sum_odd(lst):
    """
    Рекурсивно вычисляет сумму нечетных чисел в списке
    """
    # Базовый случай: пустой список
    if not lst:
        return 0
    
    # Рекурсивный случай: проверяем первый элемент
    first = lst[0]
    rest = lst[1:]
    
    if first % 2 != 0:  # Если число нечетное
        return first + sum_odd(rest)
    else:  # Если число четное
        return sum_odd(rest)

# Тестирование
print("Задача 1: Рекурсивная сумма нечетных чисел")
test_cases = [
    [1, 2, 3, 4, 5],  # 1 + 3 + 5 = 9
    [2, 4, 6],         # 0
    [1, 3, 5],         # 9
    [1, 2, 3]          # 4
]

for test in test_cases:
    print(f"sum_odd({test}) = {sum_odd(test)}")

# Проверка для n = 3 и n = 10
print(f"\nПроверка для n=3: {sum_odd([1, 2, 3])}")
print(f"Проверка для n=10: {sum_odd(list(range(1, 11)))}")
