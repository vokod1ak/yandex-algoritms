# ID успешной посылки 72779558
from typing import List, Tuple


def form_map(house_list: List[int]) -> List[int]:
    non_zero_count: int = len(house_list) - 1
    result: List[int] = [0] * len(house_list)
    for i in range(len(house_list)):
        if house_list[i] == 0:
            result[i] = 0
            non_zero_count = 1
        else:
            result[i] = non_zero_count
            non_zero_count += 1
    return result


def get_zero2(street: List[int]) -> List[int]:
    result: List[int] = [0] * len(street)
    forward_run: List[int] = form_map(street)
    backward_run: List[int] = form_map(street[::-1])
    i: int = 0
    for obj in zip(forward_run, backward_run[::-1]):
        result[i] = min(obj[0], obj[1])
        i += 1
    return result


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    street = list(map(int, input().strip().split()))
    return street, n


street, n = read_input()
result = get_zero2(street)
print(" ".join(map(str, result)))
