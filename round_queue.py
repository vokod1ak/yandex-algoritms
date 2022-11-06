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
            return print('error')

    def pop(self):
        if self.q_size == 0:
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.q_size -= 1
        return x

    def peek(self):
        return self.queue[self.head]

    def size(self):
        return self.q_size


n = int(input())
max_size = int(input())
round_q = MyQueueSized(max_size)
while n:
    command = list(map(str, input().strip().split()))
    if command[0] == 'pop':
        print(round_q.pop())
    elif command[0] == 'push':
        round_q.push(int(command[1]))
    elif command[0] == 'peek':
        print(round_q.peek())
    elif command[0] == 'size':
        print(round_q.size())
    n -= 1
