class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def empty(self):
        return self.front is None and self.back is None

    def appendleft(self, item):

        node = Node(item)
        node.next = self.front
        if not self.empty():
            self.front.prev = node
        else:
            self.back = node
        self.front = node
        self.size += 1

    def popleft(self):

        if self.empty():
            return "error"
        node = self.front
        item = node.item
        self.front = node.next
        if self.front is None:
            self.back = None
        else:
            self.front.prev = None

        del node
        self.size -= 1
        return item

    def append(self, item):
        node = Node(item)
        node.prev = self.back
        if not self.empty():
            self.back.next = node
        else:
            self.front = node
        self.back = node
        self.size += 1

    def pop(self):
        if self.empty():
            return "error"
        node = self.back
        item = node.item
        self.back = node.prev
        if self.back is None:
            self.front = None
        else:
            self.back.next = None
        del node
        self.size -= 1
        return item

    def __del__(self):
        while self.front is not None:
            node = self.front
            self.front = self.front.next
            del node
        self.back = None

    def f(self):
        if self.empty():
            return "error"
        node = self.front
        item = node.item
        return item

    def b(self):
        if self.empty():
            return "error"
        node = self.front
        item = node.item
        return item

deq = Deque()
while 1:
    enter = input().split()
    if enter[0] == "exit":
        print("bye")
        break
    elif enter[0] == "push_front":
        deq.appendleft(int(enter[1]))
        print("ok")
    elif enter[0] == "push_back":
        deq.append(int(enter[1]))
        print("ok")

    elif enter[0] == "pop_front":
        print(deq.popleft())

    elif enter[0] == "pop_back":
        print(deq.pop())

    elif enter[0] == "front":
        print(deq.f())

    elif enter[0] == "back":
        print(deq.b())

    elif enter[0] == "size":
        print(deq.size)

    elif enter[0] == "clear":
        deq = Deque()
        print("ok")
