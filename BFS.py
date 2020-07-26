class Node:
    def __init__(self, name):
        self.name = name
        self.adjencyList = []
        self.visited = False
        self.predecessor = None

class BreadthFirstSearch(object):
    def bfs(self, startNode):
        queue = []
        queue.append(startNode)
        startNode.visited = True

        while queue:
            actualNode = queue.pop(0)
            print(actualNode.name)

            for n in actualNode.adjencyList:
                if not n.visited:
                    n.visited = True
                    queue.append(n)

node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

node1.adjencyList.append(node2)
node1.adjencyList.append(node3)
node2.adjencyList.append(node4)
node4.adjencyList.append(node5)

bfs = BreadthFirstSearch()
bfs.bfs(node1)