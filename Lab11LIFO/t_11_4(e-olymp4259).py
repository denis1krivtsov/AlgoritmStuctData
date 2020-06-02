class Stack:

    def __init__(self):
        self.items = []
        self.check = False
        self.min = 10**9

    def push(self, item):
        self.items.append(item)
        if self.min > item:
            self.min = item

    def pop(self):
        if self.min == self.items[-1]:
            self.check = True
        return self.items.pop()

    def minEl(self):
        if self.check:
            min = self.items[0]
            for i in self.items:
                if min > i:
                    min = i
            self.min = min
        return self.min


n = int(input())
stack = Stack()
for i in range(n):
    st = input().split()
    if st[0] == '1':
        stack.push(int(st[1]))
    elif st[0] == '2':
        stack.pop()
    elif st[0] == '3':
        print(stack.minEl())