class Node(object):
    def __init__(self, name):
        self.name = name
        self.adjacenciesList = []
        self.visited = False
        self.predecessor = None

# BFS uses LAyer by Layer and QUEUE
# DFS uses STACK + Goes deep as possible as for each node
class DepthFirstSearch(object):
    def dfs(self, node):
        node.visited = True
        print(node.name)
        for n in node.adjacenciesList:
            if not n.visited:
                self.dfs(n)

node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

node1.adjacenciesList.append(node2)
node1.adjacenciesList.append(node3)
node2.adjacenciesList.append(node4)
node4.adjacenciesList.append(node5)

dfs = DepthFirstSearch()
dfs.dfs(node1)