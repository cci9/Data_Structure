class Node(object):

    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    # # O(logN) for balanced BST!!!!!!.....For unbalanced it could be O(N)
    def insertNode(self, data, node):
        if data < node.data:
            if node.leftchild:
                self.insertNode(data, node.leftchild)
            else:
                node.leftchild = Node(data)
        else:
            if node.rightchild:
                self.insertNode(data, node.rightchild)
            else:
                node.rightchild = Node(data)

    def getMiniValue(self):
        if self.root:
            return self.getMini(self.root)

    def getMini(self, node):
        if node.leftchild:
            return self.getMini(node.leftchild)
        return node.data

    def getMaxvalue(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self, node):
        if node.rightchild:
            return self.getMax(node.rightchild)
        return node.data

#  # O(N).....because the traversal need to search for the each element
    def traverse(self):
        if self.root:
            return self.traversalInOrder(self.root)

    def traversalInOrder(self, node):
        if node.leftchild:
            self.traversalInOrder(node.leftchild)

        print(node.data)
        if node.rightchild:
            self.traversalInOrder(node.rightchild)

# # O(logN)....the remove are required to search through the selected path
    def removeNode(self, data, node):

        if not node:
            return node

        if data < node.data:
            node.leftchild = self.removeNode(data, node.leftchild)
        elif data > node.data:
            node.rightchild = self.removeNode(data, node.rightchild)
        else:
            if not node.leftchild and not node.rightchild:
                print('Removing a leaf node...')
                del node
                return None

            if not node.leftchild:
                print('Removing a node with single right child...')
                tempNode = node.rightchild
                del node
                return tempNode

            elif not node.rightchild:
                print('Removing a node with single left child...')
                tempNode = node.leftchild
                del node
                return tempNode

            print('Removing node with  two children...')
            tempNode = self.getPredecessor(node.leftchild)
            node.data = tempNode.data
            node.leftchild = self.removeNode(tempNode.data, node.leftchild)
        return node

    def getPredecessor(self, node):

        if node.rightchild:
            return self.getPredecessor(node.rightchild)
        return node

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

bst = BinarySearchTree()
bst.insert(32)
bst.insert(10)
bst.insert(55)
bst.insert(79)
bst.insert(1)
bst.insert(19)
bst.insert(23)
bst.insert(16)

print(bst.getMaxvalue())
print(bst.getMiniValue())
print(bst.traverse())
print('\n')
bst.remove(32)
print(bst.traverse())