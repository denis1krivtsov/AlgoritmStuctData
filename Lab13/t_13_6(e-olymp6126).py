class Deque:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        return "ok"

    def pop(self):
        if self.empty():
            return "error"
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def top(self):
        if self.empty():
            return "error"
        return self.items[0]

deq = Deque()
while 1:
    enter = input().split()
    if enter[0] == "exit":
        print("bye")
        break

    elif enter[0] == "push":
        print(deq.push(int(enter[1])))

    elif enter[0] == "pop":
        print(deq.pop())

    elif enter[0] == "front":
        print(deq.top())

    elif enter[0] == "size":
        print(deq.size())

    elif enter[0] == "clear":
        deq = Deque()
        print("ok")