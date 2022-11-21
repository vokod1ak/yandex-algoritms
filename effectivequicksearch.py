# ID удачной посылки: 75599262
def partition(array, left, right):
    pivot = (array[left])
    i = left + 1
    j = right - 1
    while True:
        if i <= j and array[j] > pivot:
            j -= 1
        elif i <= j and array[i] < pivot:
            i += 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
        else:
            array[left], array[j] = array[j], array[left]
            return j


def quick_effective_search(array, left, right):
    if (right - left) > 1:
        p = partition(array, left, right)
        quick_effective_search(array, left, p)
        quick_effective_search(array, p + 1, right)


def get_member(data_list):
    name = data_list[0]
    points = data_list[1]
    penalty = data_list[2]
    return -int(points), int(penalty), name


def main():
    n = int(input())
    data = [get_member(input().strip().split()) for _ in range(n)]
    quick_effective_search(data, 0, len(data))
    for winner in data:
        print(winner[2])


if __name__ == '__main__':
    main()
