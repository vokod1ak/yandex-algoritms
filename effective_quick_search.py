# ID удачной посылки: 75856694
def quick_effective_sort2(array):
    def qsort(array, start, end):
        if start == end:
            return array
        pivot = array[start]
        left = start + 1
        right = end
        while left < right:
            if array[left] > pivot:
                if array[right] < pivot:
                    array[left], array[right] = array[right], array[left]
                else:
                    right -= 1
            else:
                left += 1
        if array[start] > array[left]:
            array[start], array[left] = array[left], array[start]
        qsort(array, start, left - 1)
        qsort(array, left, end)
        return array
    start = 0
    end = len(array) - 1
    qsort(array, start, end)
    return array


if __name__ == '__main__':
    number = int(input())
    data = [(lambda name, points, penalty: (-int(points), int(penalty), name))(*(input().split())) for _ in range(number)]
    quick_effective_sort2(data)
    print(*[name for points, penalty, name in [i for i in data]], sep='\n')
