from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def clone_graph(self, node: 'Node'):
        if node is None:
            return None
        root = node
        queue = deque([node])
        visited = {node: Node(node.val)}

        while len(queue) > 0:
            curr = queue.popleft()

            for neigh in curr.neighbors:
                # handle any newly discovered nodes
                if neigh not in visited:
                    visited[neigh] = Node(neigh.val)
                    queue.append(neigh)
                # add neighbor to current clone
                visited[curr].neighbors.append(visited[neigh])

        return visited[root]
