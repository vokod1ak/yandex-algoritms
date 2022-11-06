# ID успешной посылки 72640002

from typing import List, Tuple


def data_input() -> Tuple[int, str]:
    k: int = int(input()) * 2
    matrix: str = ''
    matrix = ''.join([matrix + input() for i in range(4)])
    return k, matrix


def play_game(matrix: str, k: int) -> int:
    numbers: List[int] = []
    score: int = 0
    for i in range(1, 10):
        count = matrix.count(str(i))
        numbers.append(count)

    for i, elem in enumerate(numbers):
        if elem == 0:
            continue
        if int(elem) <= k:
            score += 1
    return score


k, matrix = data_input()
print(play_game(matrix, k))
