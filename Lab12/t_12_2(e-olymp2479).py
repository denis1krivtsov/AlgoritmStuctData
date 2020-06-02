class Stack:
    def __init__(self):
        self.items = []
    def empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def top(self):
        return self.items[-1]

def brackerChecker(bracker_sequence):
    stack = Stack()
    for bracker in bracker_sequence:
        if bracker == "(" or bracker == "[":
            stack.push(bracker)
        elif bracker == ")":
            if stack.empty():
                return False
            elif stack.top() != "(":
                return False
            else:
                stack.pop()
        else:
            if stack.empty():
                return False
            elif stack.top() != "[":
                return False
            else:
                stack.pop()

    if stack.empty():
        return True
    return False

n = int(input())
for i in range(n):
    st = input()
    if brackerChecker(st):
        print("Yes")
    else:
        print("No")
