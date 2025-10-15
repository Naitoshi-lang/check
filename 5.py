#Сортировка имен по длине

def quicksort_names(names):
    """
    Быстрая сортировка имен по длине строки
    """
    if len(names) <= 1:
        return names
    
    # Выбираем случайный опорный элемент
    pivot_index = random.randint(0, len(names) - 1)
    pivot = names[pivot_index]
    pivot_length = len(pivot)
    
    # Разделяем по длине строки
    less = [name for i, name in enumerate(names) if len(name) < pivot_length and i != pivot_index]
    equal = [name for name in names if len(name) == pivot_length]
    greater = [name for i, name in enumerate(names) if len(name) > pivot_length and i != pivot_index]
    
    return quicksort_names(less) + equal + quicksort_names(greater)

# Тестирование
print("\nЗадача 5: Сортировка имен по длине")

names = ["Anna", "Bob", "Charlie", "Eve"]
print(f"Исходный список: {names}")

sorted_names = quicksort_names(names)
print(f"Отсортированный по длине: {sorted_names}")

# Проверка длин
print("Длины имен:")
for name in sorted_names:
    print(f"  {name}: {len(name)}")

# Дополнительный тест
more_names = ["Alice", "Tom", "Michael", "Jo", "Jennifer"]
print(f"\nДополнительный тест: {more_names}")
print(f"Отсортированный: {quicksort_names(more_names)}")
