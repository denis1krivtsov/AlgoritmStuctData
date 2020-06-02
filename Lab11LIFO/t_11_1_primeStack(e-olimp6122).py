class Stack:

    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def top(self):

        return self.items[-1]

    def push(self, item):
        self.items.append(item)
        print("ok")

    def pop(self):

        print(self.top())
        return self.items.pop()

    def __len__(self):
        return len(self.items)

stack = Stack()
while 1:
    st = input().split()
    if (len(st) == 2) and (st[0] == "push"):
        stack.push(st[1])
    elif st[0] == "pop":
        stack.pop()
    elif st[0] == "back":
        print(stack.top())
    elif st[0] == "clear":
        stack = Stack()
        print("ok")
    elif st[0] == "size":
        print(len(stack))
    elif st[0] == "exit":
        print("bye")
        break