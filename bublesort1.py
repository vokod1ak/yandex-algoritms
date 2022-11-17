def bublesort(array, lenght):
    N = lenght
    for j in range(N):
        for i in range(N - j - 1):
            if array[i] > array[i + 1]:
                array[i+1], array[i] = array[i], array[i+1]
    return array



def main():
    length = int(input())
    arr = input().split()
    print(*bublesort(arr, length))


if __name__ == '__main__':
    main()