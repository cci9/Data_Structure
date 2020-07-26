class Node(object):

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 0

class AVL(object):

    def __init__(self):

        self.root = None

    def insert(self, data):
        self.root = self.insertMethod(data, self.root)

    def insertMethod(self, data, node):
        if not node:
            return Node(data)

        if data < node.data:
            node.leftChild = self.insertMethod(data, node.leftChild)
        else:
            node.rightChild = self.insertMethod(data, node.rightChild)

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        return self.settleViolation(data, node)

    def getPredecessor(self, node):

        if node.rightChild:
            return self.getPredecessor(node.rightChild)

        return node

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def removeNode(self, data, node):

        if not node:
            return node

        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:
            if not node.leftChild and not node.rightChild:
                print('Removing a leaf node...')
                del node
                return None

            if not node.leftChild:
                print('Removing a node with a right child...')
                tempNode = node.rightChild
                del node
                return None

            elif not node.rightChild:
                print('Removing a node with a left child...')
                tempNode = node.leftChild
                del node
                return tempNode

            print('Removing node with two children...')
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)

        if not node:
            return node # if th tree had just a singe node

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        balance = self.calcBalance(node)

        # LL heavy situation
        if balance > 1 and self.calcBalance(node.leftChild) >= 0:
            return self.rotateRight(node)

        # RR heavy situation
        if balance < -1 and self.calcBalance(node.rightChild) <= 0:
            return self.rotateLeft(node)

        # LR heavy situation
        if balance > 1 and self.calcBalance(node.leftChild) < 0:
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

        # RL heavy situation
        if balance < -1 and self.calcBalance(node.rightChild) > 0:
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node


    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):

        if node.leftChild:
            self.traverseInOrder(node.leftChild)

        print("%s " % node.data)

        if node.rightChild:
            self.traverseInOrder(node.rightChild)

    def settleViolation(self, data, node):

        balance = self.calcBalance(node)

        # case 1: LL heavy situation...One R rotation of node
        if balance > 1 and data < node.leftChild.data:
            print('LL heavy situation...')
            return self.rotateRight(node)

        # case 2: RR heavy situation...One L rotation of node
        if balance < -1 and data > node.rightChild.data:
            print('RR heavy situation...')
            return self.rotateLeft(node)

        # case 3: LR heavy situation...L rotation of Childnode + R rotation of node
        if balance > 1 and data > node.leftChild.data:
            print('LR heavy situation...')
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

        # case 4: RL heavy situation...R rotation of Childnode + L rotation of node
        if balance < -1 and data < node.rightChild.data:
            print('RL heavy situation...')
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node

    def calcHeight(self, node):

        if not node:
            return -1
        return node.height

    # # if the return value > 1...left heavy tree....right rotation
    # # if the return value < -1..right heavy tree...left rotation
    def calcBalance(self, node):

        if not node:
            return 0
        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)

    def rotateRight(self, node):

        print('Rotating to the right on node:', node.data)
        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild

        tempLeftChild.rightChild = node
        node.leftChild = t

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightChild)) + 1

        return tempLeftChild

    def rotateLeft(self, node):

        print('Rotating to the left on node:', node.data)
        tempRightChild = node.rightChild
        t = tempRightChild.leftChild

        tempRightChild.leftChild = node
        node.rightChild = t

        node.height = max(self.calcHeight(node.rightChild), self.calcHeight(node.leftChild)) + 1
        tempRightChild.height = max(self.calcHeight(tempRightChild.rightChild),
                                   self.calcHeight(tempRightChild.leftChild)) + 1

        return tempRightChild

avl = AVL()
avl.insert(10)
avl.insert(20)
avl.insert(5)
avl.insert(4)
avl.insert(15)
avl.traverse()
print('\n')
avl.remove(5)
avl.remove(4)
avl.traverse()
