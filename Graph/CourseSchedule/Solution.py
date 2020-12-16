from collections import deque


class Solution:
    def can_finish(self, num_courses: int, prerequisites) -> bool:
        # calculate num prereqs (indegrees) of each course
        # create an adjacency list for each node to their neighbors
        indegrees = {}
        adjacency_list = {}
        for course in range(num_courses):
            indegrees[course] = 0
            adjacency_list[course] = []

        for prereq in prerequisites:
            # a prereq is -> { course: prereq course }
            indegrees[prereq[0]] += 1
            adjacency_list[prereq[1]].append(prereq[0])

        # find all courses without any prereqs (source nodes)
        source_nodes = deque([])
        for node, ind in indegrees.items():
            if ind == 0:
                source_nodes.append(node)

        # BFS traversal through digraph
        # add all current source nodes to topological ordering
        topological_ordering = []
        while len(source_nodes) > 0:
            node = source_nodes.popleft()
            topological_ordering.append(node)

            for neighbor in adjacency_list[node]:
                # reduce its neighbors' indegrees by 1 bc we removed that source node
                indegrees[neighbor] -= 1
                # check if removed source node's neighbors have become source nodes too
                # and add them to queue if so
                if indegrees[neighbor] == 0:
                    source_nodes.append(neighbor)

        # if the topological ordering is the same length as num nodes
        # in original graph, then we have found a success
        if len(topological_ordering) == num_courses:
            return True
        return False
