# ID удачной посылки: 73926592

class DequeIsFullError(Exception):

    def __init__(self):
        super().__init__('error')


class DequeIsEmptyError(Exception):

    def __init__(self):
        super().__init__('error')


class Deque:
    def __init__(self, max_size):
        self._max_n = max_size
        self._queue = [None] * self._max_n
        self._head = 0
        self._tail = 0
        self._q_size = 0

    def _is_empty(self):
        return self._q_size == 0

    def push_front(self, item):
        if self._q_size != self._max_n:
            self._queue[self._head - 1] = item
            self._head = (self._head - 1) % self._max_n
            self._q_size += 1
        else:
            raise DequeIsFullError

    def push_back(self, item):
        if self._q_size != self._max_n:
            self._queue[self._tail] = item
            self._tail = (self._tail + 1) % self._max_n
            self._q_size += 1
        else:
            raise DequeIsFullError

    def pop_front(self):
        if self._is_empty():
            raise DequeIsEmptyError
        x = self._queue[self._head]
        self._queue[self._head] = None
        self._head = (self._head + 1) % self._max_n
        self._q_size -= 1
        return x

    def pop_back(self):
        if self._is_empty():
            raise DequeIsEmptyError
        x = self._queue[self._tail - 1]
        self._queue[self._tail - 1] = None
        self._tail = (self._tail - 1) % self._max_n
        self._q_size -= 1
        return x


def comm_handler(dek_q):
    cmd, *args = input().split()
    try:
        return getattr(dek_q, cmd)(*args)
    except AttributeError:
        raise ValueError('Invalid input')
    except (DequeIsFullError, DequeIsEmptyError):
        return 'error'


def main():
    n = int(input())
    max_size = int(input())
    dek_q = Deque(max_size)
    for _ in range(n):
        result = comm_handler(dek_q)
        if result:
            print(result)


if __name__ == '__main__':
    main()
