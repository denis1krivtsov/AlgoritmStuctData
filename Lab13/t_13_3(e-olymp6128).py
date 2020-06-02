class Deque:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push_front(self, item):
        self.items.insert(0, item)
        print("ok")

    def push_back(self, item):
        self.items.append(item)
        print("ok")

    def pop_front(self):
        if self.empty():
            return "error"
        return self.items.pop(0)

    def pop_back(self):
        if self.empty():
            return "error"
        return self.items.pop()

    def front(self):
        if self.empty():
            return "error"
        return self.items[0]

    def back(self):
        if self.empty():
            return "error"
        return self.items[-1]

    def size(self):
        return len(self.items)

deq = Deque()
while 1:
    enter = input().split()
    if enter[0] == "exit":
        print("bye")
        break
    elif enter[0] == "push_front":
        deq.push_front(int(enter[1]))
    elif enter[0] == "push_back":
        deq.push_back(int(enter[1]))

    elif enter[0] == "pop_front":
        print(deq.pop_front())
    elif enter[0] == "pop_back":
        print(deq.pop_back())

    elif enter[0] == "front":
        print(deq.front())
    elif enter[0] == "back":
        print(deq.back())
    elif enter[0] == "size":
        print(deq.size())

    elif enter[0] == "clear":
        deq = Deque()
        print("ok")
