class ListQueue:
    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

        def __str__(self):
            return self.value

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.q_size = 0

    def is_empty(self):
        return self.q_size == 0

    def get(self):
        if self.is_empty():
            return 'error'
        if self.q_size == 1:
            x = self.head.value
            self.head = self.Node()
            self.tail = self.Node()
            self.q_size -= 1
            return x
        if self.q_size == 2:
            x = self.head.value
            self.head = self.tail
            self.q_size -= 1
            return x
        x = self.head.value
        self.head = self.tail.next.next
        self.tail.next = self.head
        self.q_size -= 1
        return x

    def put(self, x):
        if self.q_size == 0:
            self.head = self.Node(value=x)
            self.tail = self.head
        else:
            self.tail.next = self.Node(value=x)
            self.tail.next.next = self.head
            self.tail = self.tail.next
        self.q_size += 1

    def size(self):
        return self.q_size


n = int(input())
q = ListQueue()
while n:
    command = list(map(str, input().strip().split()))
    if command[0] == 'get':
        print(q.get())
    elif command[0] == 'put':
        q.put(int(command[1]))
    elif command[0] == 'size':
        print(q.size())
    n -= 1
