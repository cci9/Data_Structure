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

    def reverse(self):

        current_node = self.head
        previous_node = None
        next_node = None

        while current_node is not None:
            next_node = current_node.nextNode
            current_node.nextNode = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node


llist = LinkedList()
llist.insertionStart(5)
llist.insertionStart(20)
llist.insertionStart(2)
llist.insertionStart(15)
llist.insertionStart(30)
llist.insertionStart(0)
llist.traverseList()

llist.reverse()
llist.traverseList()
