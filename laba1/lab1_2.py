from typing import List, Optional, Tuple

# Task 1: n-е простое число
def is_prime(k: int) -> bool:
    if k <= 1:
        return False
    if k <= 3:
        return True
    if k % 2 == 0:
        return False
    i = 3
    while i * i <= k:
        if k % i == 0:
            return False
        i += 2
    return True


def prime(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n должно быть целым числом")
    if n <= 0:
        raise ValueError("n должно быть положительным")
    count = 0
    candidate = 1
    while count < n:
        candidate += 1
        if is_prime(candidate):
            count += 1
    return candidate

# Task 3: первый столбец с все элементами отрицательными
def first_negative_column(matrix: List[List[float]]) -> Optional[Tuple[int, float]]:
    if not matrix:
        return None
    row_count = len(matrix)
    col_count = len(matrix[0])
    for r in matrix:
        if len(r) != col_count:
            raise ValueError("Все строки матрицы должны быть одинаковой длины")

    for col in range(col_count):
        all_negative = True
        s = 0.0
        for row in range(row_count):
            val = matrix[row][col]
            if val >= 0:
                all_negative = False
                break
            s += val
        if all_negative:
            mean = s / row_count
            return col, mean
    return None

# Task 4: демонстрация try/except/finally
def demo_try_except_finally_examples() -> List[str]:
    results = []
    try:
        a = 10
        b = 2
        c = a / b
        results.append(f"A: {a} / {b} = {c}")
    except ZeroDivisionError:
        results.append("A: Деление на ноль")
    finally:
        results.append("A: Выполнен блок finally")

    try:
        a = 5
        b = 0
        c = a / b
        results.append(f"B: {a} / {b} = {c}")
    except ZeroDivisionError as ex:
        results.append(f"B: Поймано ZeroDivisionError: {ex}")
    finally:
        results.append("B: Выполнен блок finally")

    try:
        raise ValueError("демонстрационный ValueError")
    except ValueError as ex:
        results.append(f"C: Поймано ValueError: {ex}")
    finally:
        results.append("C: Выполнен блок finally (cleanup C)")

    try:
        value = undefined_variable
        results.append(f"D: value = {value}")
    except Exception as ex:
        results.append(f"D: Поймано Exception: {type(ex).__name__}: {ex}")
    finally:
        results.append("D: Выполнен блок finally (cleanup D)")

    return results

print("Задание 1: prime(n) — n-е простое число")
for i in range(1, 11):
    p = prime(i)
    print(f"prime({i}) = {p}")

print("Задание 3: first_negative_column(matrix) — первый столбец с все элементами отрицательными")
matrices = [
    [[1, -2, -3],
     [-4, -5, -6],
     [7, -8, -9]],
    [[-1, 2, -3],
     [-2, 0, -5],
     [-3, 4, -6]],
    [[1, 2],
     [3, 4],
     [5, 6]],
    ]

for idx, mat in enumerate(matrices, start=1):
    res = first_negative_column(mat)
    print(f"матрица #{idx}: результат = {res}")

print("Задание 4: демонстрация try/except/finally")
demo_res = demo_try_except_finally_examples()
for line in demo_res:
    print(line)
