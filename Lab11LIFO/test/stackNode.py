class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self):
        self.top_node = None

    def empty(self):
        return self.top_node is None

    def push(self, item):
""" Створюємо новий вузол стеку
    Якщо стек не порожній, то новий вузол
    має посилатися на поточну верхівку"""
        new_node = Node(item)
        if not empty:
            new_node.next = self.top_node
        self.top_node = new_node

    def pop(self):
        """ Забирає верхівку стека
        Сам вузол при цьому прибирається зі стеку
        :return: Навантаження верхівки стеку"""
        if self.empty():
            raise Exception("empty true")
        current_node = self.top_node
        item = current_node.item
        self.top_node = self.top_node.next
        del current_node
        return item

    def top(self):
        if self.empty():
            raise Exception("empty true")
        return self.top_node.item

