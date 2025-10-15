#Рекурсивный поиск ключа 

def find_key(boxes):
    """
    Рекурсивно ищет ключ в структуре коробок
    """
    # Базовый случай: нашли ключ
    if boxes == "key":
        return "Ключ найден!"
    
    # Базовый случай: пустой список или не список
    if not isinstance(boxes, list) or not boxes:
        return "Ключ не найден"
    
    # Рекурсивный случай: проверяем каждый элемент
    for item in boxes:
        result = find_key(item)
        if result == "Ключ найден!":
            return result
    
    return "Ключ не найден"

# Тестирование
print("\nЗадача 2: Рекурсивный поиск ключа")

test_cases = [
    [["box1", ["box2", "key"]], "box3"],           # Ключ найден
    [["box1", ["box2", "key"]], ["box3", "box4"]], # Ключ найден  
    [["box1", "box2"], "box3"],                    # Ключ не найден
    ["key"],                                       # Ключ найден
    [[["box1", "box2"], ["box3"]], "box4"]         # Ключ не найден
]

for i, test in enumerate(test_cases, 1):
    print(f"Тест {i}: {test} -> {find_key(test)}")
