#Быстрая сортировка (первый элемент как опорный)

def quicksort(arr):
    """
    Реализация быстрой сортировки с первым элементом как опорным
    """
    # Базовый случай: массивы длиной 0 или 1 уже отсортированы
    if len(arr) <= 1:
        return arr
    
    # Выбираем первый элемент как опорный
    pivot = arr[0]
    
    # Разделяем на элементы меньше, равные и больше опорного
    less = [x for x in arr[1:] if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr[1:] if x > pivot]
    
    # Рекурсивно сортируем и объединяем
    return quicksort(less) + equal + quicksort(greater)

# Тестирование
print("\nЗадача 3: Быстрая сортировка")
test_arr = [10, 7, 8, 1, 5]
print(f"Исходный массив: {test_arr}")
print(f"Отсортированный: {quicksort(test_arr)}")

# Дополнительные тесты
test_arrays = [
    [64, 34, 25, 12, 22, 11, 90],
    [5, 2, 4, 6, 1, 3],
    [1],
    []
]

for arr in test_arrays:
    print(f"quicksort({arr}) = {quicksort(arr)}")
