from typing import Any, Iterable, List as TypeList, Optional, Tuple, Dict
import math
import datetime

# Задание 1: класс List
class List:
    def __init__(self, initial: Optional[Iterable[Any]] = None):
        self._items: TypeList[Any] = list(initial) if initial is not None else []

    def append(self, item: Any) -> None:
        self._items.append(item)

    def insert(self, index: int, item: Any) -> None:
        if index < 0:
            raise IndexError("Индекс не может быть отрицательным")
        if index >= len(self._items):
            self._items.append(item)
        else:
            self._items.insert(index, item)

    def remove_at(self, index: int) -> Any:
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")
        return self._items.pop(index)

    def remove_value(self, value: Any) -> bool:
        try:
            self._items.remove(value)
            return True
        except ValueError:
            return False

    def get(self, index: int) -> Any:
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")
        return self._items[index]

    def size(self) -> int:
        return len(self._items)

    def find(self, value: Any) -> int:
        try:
            return self._items.index(value)
        except ValueError:
            return -1

    def clear(self) -> None:
        self._items.clear()

    def to_list(self) -> TypeList[Any]:
        return list(self._items)

    def __str__(self) -> str:
        return f"List({self._items})"

    def __iter__(self):
        return iter(self._items)


def task1_list_demo() -> None:
    print("Задание 1: демонстрация класса List")
    l = List([1, 2, 3])
    print("Инициализация:", l)

    l.append(4)
    print("После вставки 4:", l)

    l.insert(1, 9)
    print("После вставки 1, 9:", l)

    removed = l.remove_at(2)
    print(f"После remove_at(2) удалено={removed}, сейчас:", l)

    found_index = l.find(9)
    print("find(9) ->", found_index)

    removed_bool = l.remove_value(100)
    print("remove_value(100) ->", removed_bool)

    removed_bool2 = l.remove_value(9)
    print("remove_value(9) ->", removed_bool2, "сейчас:", l)

    print("get(0) ->", l.get(0))
    print("size() ->", l.size())

    l.clear()
    print("После clear():", l, "размер:", l.size())

# Задание 2: транспорт
class Vehicle:
    def __init__(self, name: str, speed_kmh: float, cost_per_km: float):
        self.name = name
        self.speed_kmh = speed_kmh
        self.cost_per_km = cost_per_km

    def move(self) -> str:
        return f"{self.name}: перемещение обычным способом."

    def compute_trip(self, origin: str, dest: str, distance_km: float) -> Tuple[float, float]:
        if distance_km < 0:
            raise ValueError("Расстояние не может быть отрицательным")
        time_hours = distance_km / self.speed_kmh if self.speed_kmh > 0 else float('inf')
        cost = distance_km * self.cost_per_km
        return time_hours, cost

    def __str__(self):
        return f"{self.name} (скорость={self.speed_kmh} км/ч, стоимость/км={self.cost_per_km})"


class Airplane(Vehicle):
    def __init__(self, name="Самолет", speed_kmh=800.0, cost_per_km=0.25, landing_fee=30.0):
        super().__init__(name, speed_kmh, cost_per_km)
        self.landing_fee = landing_fee

    def move(self) -> str:
        return f"{self.name}: летит по воздуху."

    def compute_trip(self, origin: str, dest: str, distance_km: float) -> Tuple[float, float]:
        base_time, base_cost = super().compute_trip(origin, dest, distance_km)
        cost = base_cost + self.landing_fee
        discount = math.floor(distance_km / 1000) * 0.01 * base_cost
        cost -= discount
        return base_time, max(cost, 0.0)


class Train(Vehicle):
    def __init__(self, name="Поезд", speed_kmh=120.0, cost_per_km=0.08, ticket_fee=5.0):
        super().__init__(name, speed_kmh, cost_per_km)
        self.ticket_fee = ticket_fee

    def move(self) -> str:
        return f"{self.name}: едет по рельсам."

    def compute_trip(self, origin: str, dest: str, distance_km: float) -> Tuple[float, float]:
        time, cost = super().compute_trip(origin, dest, distance_km)
        cost = cost + self.ticket_fee
        return time, cost


class Car(Vehicle):
    def __init__(self, name="Car", speed_kmh=80.0, cost_per_km=0.12, fixed_fee=0.0, traffic_factor=1.1):
        super().__init__(name, speed_kmh, cost_per_km)
        self.fixed_fee = fixed_fee
        self.traffic_factor = traffic_factor

    def move(self) -> str:
        return f"{self.name}: едет по дороге."

    def compute_trip(self, origin: str, dest: str, distance_km: float) -> Tuple[float, float]:
        base_time, base_cost = super().compute_trip(origin, dest, distance_km)
        time = base_time * self.traffic_factor
        cost = base_cost + self.fixed_fee
        return time, cost

DISTANCES: Dict[Tuple[str, str], float] = {
    ("Вильнюс", "Рига"): 260.0,
    ("Вильнюс", "Warsaw"): 450.0,
    ("Рига", "Таллин"): 310.0,
    ("Варшава", "Берлин"): 570.0,
    ("Вильнюс", "Берлин"): 600.0,
    ("Рига", "Варшава"): 670.0,
    ("Берлин", "Хельсинки"): 80.0,
    ("Вильнюс", "Берлин"): 930.0,
}

def get_distance(a: str, b: str) -> Optional[float]:
    if (a, b) in DISTANCES:
        return DISTANCES[(a, b)]
    if (b, a) in DISTANCES:
        return DISTANCES[(b, a)]
    return None


def find_best_options(vehicles: Iterable[Vehicle], origin: str, dest: str) -> Tuple[Optional[Tuple[Vehicle, float, float]], Optional[Tuple[Vehicle, float, float]]]:
    distance = get_distance(origin, dest)
    if distance is None:
        print(f"Расстояние между {origin} и {dest} неизвестно.")
        return None, None

    fastest: Optional[Tuple[Vehicle, float, float]] = None
    cheapest: Optional[Tuple[Vehicle, float, float]] = None

    for v in vehicles:
        time_h, cost = v.compute_trip(origin, dest, distance)
        if fastest is None or time_h < fastest[1]:
            fastest = (v, time_h, cost)
        if cheapest is None or cost < cheapest[2]:
            cheapest = (v, time_h, cost)

    return fastest, cheapest


def format_time(hours: float) -> str:
    if math.isinf(hours):
        return "н/д"
    h = int(hours)
    m = int(round((hours - h) * 60))
    return f"{h} ч {m} мин"


def save_report(filename: str, origin: str, dest: str, fastest: Optional[Tuple[Vehicle, float, float]], cheapest: Optional[Tuple[Vehicle, float, float]], all_results: TypeList[Tuple[Vehicle, float, float]]) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Отчет\n")
        f.write(f"Из: {origin} в: {dest}\n")
        f.write(f"Дата создания: {datetime.datetime.now().isoformat()}\n\n")
        f.write("Транспорт:\n")
        for v, t, c in all_results:
            f.write(f"  {v.name}: время={format_time(t)}, стоимость={c:.2f}\n")
        f.write("\n")
        if fastest:
            f.write(f"Быстрее: {fastest[0].name} — время={format_time(fastest[1])}, стоимость={fastest[2]:.2f}\n")
        else:
            f.write("Быстрее: n/a\n")
        if cheapest:
            f.write(f"Дешевле: {cheapest[0].name} — время={format_time(cheapest[1])}, стоимость={cheapest[2]:.2f}\n")
        else:
            f.write("Дешевле: n/a\n")
    print(f"Отчет сохранен в {filename}")


def task2_transport_demo() -> None:
    print("Задание 2: демонстрация транспорта")
    origin = "Вильнюс"
    dest = "Рига"

    vehicles = [
        Airplane(name="Boeing", speed_kmh=850.0, cost_per_km=0.30, landing_fee=40.0),
        Train(name="БелЖД", speed_kmh=140.0, cost_per_km=0.07, ticket_fee=3.0),
        Car(name="Лада веста", speed_kmh=90.0, cost_per_km=0.13, fixed_fee=0.0, traffic_factor=1.15),
    ]

    distance = get_distance(origin, dest)
    if distance is None:
        return

    print(f"Расстояние {origin} -> {dest} = {distance} км")

    all_results: TypeList[Tuple[Vehicle, float, float]] = []
    for v in vehicles:
        t, c = v.compute_trip(origin, dest, distance)
        all_results.append((v, t, c))
        print(f"{v.name}: {v.move()}  время={format_time(t)}, стоимость={c:.2f}")

    fastest, cheapest = find_best_options(vehicles, origin, dest)

    if fastest:
        v, t, c = fastest
        print(f"\nБыстрее: {v.name} — время={format_time(t)}, стоимость={c:.2f}")
    else:
        print("n/a")

    if cheapest:
        v2, t2, c2 = cheapest
        print(f"Дешевле: {v2.name} — время={format_time(t2)}, стоимость={c2:.2f}")
    else:
        print("n/a")

    save_report("trip_report.txt", origin, dest, fastest, cheapest, all_results)

task1_list_demo()
task2_transport_demo()
