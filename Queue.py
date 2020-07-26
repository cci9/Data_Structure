class Queue:

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def denqueue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        return self.queue[0]

    def size_(self):
        return len(self.queue)

    def print_(self):
        return self.queue

array = Queue()
print(array.isEmpty())
array.enqueue(10)
array.enqueue(20)
array.enqueue(30)
array.enqueue(40)
print(array.print_())
print(array.denqueue())
print(array.print_())
print(array.peek())

