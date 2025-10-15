#Оптимизированная быстрая сортировка (случайный опорный элемент)

import random
import time

def quicksort_optimized(arr):
    """
    Оптимизированная быстрая сортировка со случайным опорным элементом
    """
    if len(arr) <= 1:
        return arr
    
    # Выбираем случайный опорный элемент
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    
    # Разделяем массив
    less = [x for i, x in enumerate(arr) if x < pivot and i != pivot_index]
    equal = [x for x in arr if x == pivot]
    greater = [x for i, x in enumerate(arr) if x > pivot and i != pivot_index]
    
    return quicksort_optimized(less) + equal + quicksort_optimized(greater)

# Сравнение производительности
print("\nЗадача 4: Оптимизированная быстрая сортировка")

# Тестируем на отсортированном массиве
sorted_arr = [1, 2, 3, 4, 5]
print(f"Исходный отсортированный массив: {sorted_arr}")

# Оригинальная версия (первый элемент как опорный)
start_time = time.time()
result1 = quicksort(sorted_arr.copy())
time1 = time.time() - start_time

# Оптимизированная версия (случайный опорный элемент)
start_time = time.time()
result2 = quicksort_optimized(sorted_arr.copy())
time2 = time.time() - start_time

print(f"Оригинальная версия: {result1}, время: {time1:.6f} сек")
print(f"Оптимизированная версия: {result2}, время: {time2:.6f} сек")

# Тестируем на случайном массиве
random_arr = [random.randint(1, 100) for _ in range(1000)]
print(f"\nТест на массиве из 1000 случайных элементов:")

start_time = time.time()
quicksort(random_arr.copy())
time1 = time.time() - start_time

start_time = time.time()
quicksort_optimized(random_arr.copy())
time2 = time.time() - start_time

print(f"Оригинальная версия: {time1:.6f} сек")
print(f"Оптимизированная версия: {time2:.6f} сек")
