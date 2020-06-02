class Stack:

    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def top(self):
        if self.empty():
            raise Exception("sdsdsdsdsdsd")
        return self.items[-1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.empty():
            raise Exception("555")
        return self.items.pop()

    def __len__(self):
        return len(self.items)

def convert(dec_number, digit = 16):
    stack = Stack()
    while dec_number > 0:
        stack.push(dec_number % digit)
        dec_number //= digit
    converted = ""
    ch = False
    while not stack.empty():
        converted = converted + get_char_digit(stack.pop())
    return converted

def get_char_digit(digit):
    if digit < 9:
        str_digit = str(digit)
    else:
        str_digit = chr(ord("A") + digit - 10)
    return str_digit

def char_digit(n, digit=2):
    new_n = 0
    ln = len(n)
    for el in n:
        new_n += int(el)*(2**(ln-1))
        ln -= 1
    return new_n

if __name__ == "__main__":
    n = list(input())
    print(convert(char_digit(n)))
    #print(char_digit(convert(14545, 2)))



