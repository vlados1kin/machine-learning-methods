import re
from typing import List, Dict, Any

# Task 1: seconds -> D:HH:MM:SS
def task1(seconds: int = 100000) -> str:
    if not isinstance(seconds, int):
        raise TypeError("Секунды должны быть целым числом")
    if seconds < 0:
        raise ValueError("Секунды не могут быть отрицательными")

    days = seconds // 86400
    rem = seconds % 86400
    hours = rem // 3600
    rem = rem % 3600
    minutes = rem // 60
    secs = rem % 60

    result = f"{days}:{hours:02d}:{minutes:02d}:{secs:02d}"
    print("Задание 1 — секунды -> ДД:ЧЧ:ММ:СС")
    print(f" Введено секунд: {seconds}")
    print(f" Результат: {result}")
    return result

# Task 2: найти все числа в строке
def task2(text: str = "В примере: 123 и -45.6, также 007 и +12") -> List[str]:
    print("\nЗадание 2 — найти числа в строке")
    print(f" Введена строка: {text}")

    pattern = re.compile(r'[-+]?\d+(?:\.\d+)?')
    matches = pattern.findall(text)

    print(" Числа:", matches)
    return matches

# Task 3: посчитать гласные/согласные в словах списка
def task3(items: List[Any] = None) -> Dict[str, Dict[str, int]]:
    print("\nЗадание 3 — гласные и согласные в строковых элементах списка")
    if items is None:
        items = ['Python', 15442, 32, 'QweRty', 34, 19, 'love']

    vowels = set("aeiouyAEIOUY")
    results: Dict[str, Dict[str, int]] = {}

    print(" Введен список:", items)
    for el in items:
        if not isinstance(el, str):
            continue
        word = el
        v = 0
        c = 0
        for ch in word:
            if not ch.isalpha():
                continue
            if ch in vowels:
                v += 1
            else:
                c += 1
        results[word] = {"гласные": v, "согласные": c}
        print(f"  '{word}': гласные={v}, согласные={c}")

    return results

# Task 4: слияние нескольких словарей в один
def task4(dicts: List[Dict[Any, Any]] = None) -> Dict[Any, Any]:
    print("\nЗадание 4 — слияние нескольких словарей")
    if dicts is None:
        dicts = [
            {"a": 1, "b": 2},
            {"b": 3, "c": 4},
            {"a": 5, "d": "x"}
        ]
    print(" Введены словари:", dicts)

    merged: Dict[Any, Any] = {}
    for d in dicts:
        if not isinstance(d, dict):
            raise TypeError("Все элементы должны быть словарями")
        for k, v in d.items():
            merged[k] = v

    print(" Результат:", merged)
    return merged

task1(100000)
task2("В строке встречаются числа: 42, -3.5, 007 и +12")
task3()
task4()
