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

    def traverseList(self):
        actualNode = self.head
        while actualNode is not None:
            print(actualNode.data)
            actualNode = actualNode.nextNode

    def get_middle_node(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer.nextNode and fast_pointer.nextNode.nextNode:
            fast_pointer = fast_pointer.nextNode.nextNode
            slow_pointer = slow_pointer.nextNode

        return slow_pointer

llist = LinkedList()
llist.insertionStart(5)
llist.insertionStart(20)
llist.insertionStart(2)
llist.insertionStart(15)
llist.insertionStart(30)
llist.insertionStart(0)
llist.traverseList()
print(llist.get_middle_node().data)