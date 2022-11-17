def sort_start(arr):
    n = len(arr)
    if n == 1:
        return arr
    else:
        middle = int(len(arr) / 2)
        left = sort_start(arr[:middle])
        right = sort_start(arr[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0][0] <= right[0][0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result

def merge_clumbs(arr):
    N = len(arr)
    total = []
    start, end = arr[0]
    i = 1
    while i < N:
        if start <= arr[i][0] <= end:
            _, curr_end = arr[i]
            i += 1
            if curr_end > end:
                end = curr_end
        else:
            total.append([start, end])
            start, end = arr[i]
            i += 1
    total.append([start, end])
    return total


def main():
    workers = int(input())
    coords = []
    for _ in range(workers):
        coords.append(list(map(int, input().split())))
    # coords = sort_start(coords)
    coords.sort()
    results = merge_clumbs(coords)
    for res in results:
        print(*res)


if __name__ == '__main__':
    main()
