def bublesort(array):
    N = len(array)
    for j in range(N):
        for i in range(N - j - 1):
            num1 = array[i] + array[i + 1]
            num2 = array[i + 1] + array[i]
            if num1 < num2:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array


def main():
    length = int(input())
    arr = input().strip().split()
    res = bublesort(arr)
    print(''.join(res))


if __name__ == '__main__':
    main()
