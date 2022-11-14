from typing import List, Tuple


def binarySearch(arr: List[int], x: int, left: int, right: int) -> int:
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] >= x > arr[mid - 1] or mid == 0:
        return mid + 1
    elif x <= arr[mid]:
        return binarySearch(arr, x, left, mid)
    else:
        return binarySearch(arr, x, mid + 1, right)


def main():
    days = int(input())
    summ = list(map(int, input().strip().split()))
    price = int(input())
    result = []
    result.append(binarySearch(summ, price, left=0, right=len(summ)))
    result.append(binarySearch(summ, 2 * price, left=0, right=len(summ)))
    print(*result)


if __name__ == '__main__':
    main()