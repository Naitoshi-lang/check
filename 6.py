#Сортировка температур по убыванию


def quicksort_temps(temps):
    """
    Быстрая сортировка температур по убыванию
    """
    if len(temps) <= 1:
        return temps
    
    # Выбираем случайный опорный элемент
    pivot_index = random.randint(0, len(temps) - 1)
    pivot = temps[pivot_index]
    
    # Разделяем для сортировки по убыванию
    greater = [temp for i, temp in enumerate(temps) if temp > pivot and i != pivot_index]
    equal = [temp for temp in temps if temp == pivot]
    less = [temp for i, temp in enumerate(temps) if temp < pivot and i != pivot_index]
    
    return quicksort_temps(greater) + equal + quicksort_temps(less)

# Тестирование
print("\nЗадача 6: Сортировка температур по убыванию")

temps = [22, 18, 25, 20, 23, 19, 21]
print(f"Исходные температуры: {temps}")

sorted_temps = quicksort_temps(temps)
print(f"Отсортированные по убыванию: {sorted_temps}")

# Проверка ожидаемого результата
expected = [25, 23, 22, 21, 20, 19, 18]
print(f"Ожидаемый результат: {expected}")
print(f"Результат корректный: {sorted_temps == expected}")

# Дополнительный тест
more_temps = [30, 15, 28, 22, 35, 19, 26, 24]
print(f"\nДополнительный тест: {more_temps}")
print(f"Отсортированные: {quicksort_temps(more_temps)}")
