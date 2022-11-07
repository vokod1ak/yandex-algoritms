class QueueIsFullError(Exception):
    pass


class QueueIsEmptyError(Exception):
    pass


class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.current_max = []

    def push(self, item):
        if self.items:
            if item >= self.current_max[-1]:
                self.items.append(item)
                self.current_max.append(item)
                self.current_max = list(sorted(self.current_max))
            else:
                self.items.append(item)
        else:
            self.items.append(item)
            self.current_max.append(item)

    def pop(self):
        if self.items:
            if self.items[-1] == self.current_max[-1]:
                self.items.pop(-1)
                self.current_max.pop(-1)
            else:
                self.items.pop()
        else:
            raise QueueIsEmptyError

    def get_max(self):
        if self.items:
            return self.current_max[-1]
        return None


def comm_handler(dek_q):
    cmd, *args = input().split()
    try:
        if args:
            return getattr(dek_q, cmd)(int(*args))
        else:
            return getattr(dek_q, cmd)(*args)
    except AttributeError:
        raise ValueError('Invalid input')
    except QueueIsFullError:
        return 'error'
    except QueueIsEmptyError:
        return None


n = int(input())
stack = StackMaxEffective()
for _ in range(n):
    for _ in range(n):
        result = comm_handler(stack)
        if result:
            print(result)