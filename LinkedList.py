class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    # O(1) complexity
    def insertionStart(self, data):
        self.size = self.size + 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    # O(1)
    def size1(self):
        return self.size

    # O(N)
    def size2(self):
        actualNode = self.head
        size = 0
        while actualNode is not None:
             size += 1
             actualNode = actualNode.nextNode
        return size

    # O(N)
    def insertionEnd(self, data):
        self.size += 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        actualNode.nextNode = newNode

    # O(N)
    def traverseList(self):
        actualNode = self.head
        while actualNode is not None:
            print(actualNode.data)
            actualNode = actualNode.nextNode

    # O(N)
    def remove(self, removeData):

        if self.head is None:
            return

        self.size -= 1
        currentNode = self.head
        previousNode = None

        while currentNode.data != removeData:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode


llist = LinkedList()
llist.insertionStart(5)
llist.insertionEnd(15)
llist.insertionStart(20)
llist.traverseList()
print(llist.size1())
print(llist.size2())
llist.remove(15)
print('\n')
llist.traverseList()