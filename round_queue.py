class QueueIsFullError(Exception):
    pass


class QueueIsEmptyError(Exception):
    pass


class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.q_size = 0

    def push(self, item):
        if self.q_size != self.max_n:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_n
            self.q_size += 1
        else:
            raise QueueIsFullError

    def pop(self):
        if self.q_size == 0:
            raise QueueIsEmptyError
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.q_size -= 1
        return x

    def peek(self):
        return self.queue[self.head]

    def size(self):
        return self.q_size


def comm_handler(dek_q):
    cmd, *args = input().split()
    try:
        return getattr(dek_q, cmd)(*args)
    except AttributeError:
        raise ValueError('Invalid input')
    except QueueIsFullError:
        return 'error'
    except QueueIsEmptyError:
        return None


def main():
    n = int(input())
    max_size = int(input())
    round_q = MyQueueSized(max_size)
    for _ in range(n):
        result = comm_handler(round_q)
        if result:
            print(result)


if __name__ == '__main__':
    main()