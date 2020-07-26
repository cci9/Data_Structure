class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def size_(self):
        return len(self.stack)

    def print_(self):
        return self.stack

array = Stack()
print(array.isEmpty())
array.push(10)
array.push(20)
array.push(30)
array.push(40)
print(array.print_())
print(array.pop())
print(array.print_())
print(array.peek())

