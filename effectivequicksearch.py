def quick_effective_search(data):
    pass


def get_member(data_list):
    name = data_list[0]
    points = data_list[1]
    penalty = data_list[2]
    return name, int(points), int(penalty)


def main():
    n = int(input())
    data = [get_member(input().strip().split()) for _ in range(n)]


if __name__ == '__main__':
    main()