class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.current_max = []

    def push(self, item):
        if self.items:
            if item >= self.current_max[-1]:
                self.items.append(item)
                self.current_max.append(item)
            else:
                self.items.append(item)
        else:
            self.items.append(item)
            self.current_max.append(item)

    def pop(self):
        if self.items:
            if self.items[-1] == self.current_max[-1]:
                self.items.pop()
                self.current_max.pop()
            else:
                self.items.pop()
        else:
            print('error')

    def get_max(self):
        if self.items:
            return self.current_max[-1]
        return None

n = int(input())
stack = StackMaxEffective()
for _ in range(n):
    command = list(map(str, input().strip().split()))
    if command[0] == 'pop':
        stack.pop()
    elif command[0] == 'push':
        stack.push(int(command[1]))
    elif command[0] == 'get_max':
        print(stack.get_max())