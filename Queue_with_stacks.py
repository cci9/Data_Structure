class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, data):
        self.enqueue_stack.append(data)

    def dequeue(self):
        if len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0:
            raise Exception('stacks are empty...')

        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) != 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())

        return self.dequeue_stack.pop()

queue = Queue()
queue.enqueue(10)
queue.enqueue(5)
queue.enqueue(20)

print(queue.dequeue())
queue.enqueue(100)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())


