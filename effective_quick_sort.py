# ID удачной посылки: 75925766
def quick_effective_sort(array):
    def _partition(start, end):
        count = start - 1
        pivot = array[end]
        step = start
        while step < end:
            if array[step] < pivot:
                count += 1
                array[count], array[step] = array[step], array[count]
            step += 1
        array[count + 1], array[end] = array[end], array[count + 1]
        return count + 1

    def _qsort(start, end):
        if start > end:
            return array
        pivot_ind = _partition(start, end)
        _qsort(start, pivot_ind - 1)
        _qsort(pivot_ind + 1, end)
        return array

    return _qsort(0, len(array) - 1)


if __name__ == '__main__':
    number = int(input())
    data = [(lambda name, points, penalty:
             (-int(points), int(penalty), name))
            (*(input().split())) for _ in range(number)]
    quick_effective_sort(data)
    print(*[name for _, _, name in data], sep='\n')
