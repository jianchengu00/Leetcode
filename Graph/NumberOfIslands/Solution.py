from collections import deque


class Solution:
    def num_islands(self, grid) -> int:
        # max island size
        num_island = 0

        # track what islands were already visited
        visited = [[False for col in grid[0]] for row in grid]

        # go through every point and run BFS if we hit an unvisited island (1)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and visited[i][j] == False:
                    # run BFS to mark all the adjacent set of 1s as visited
                    num_island += self.bfs(i, j, grid, visited)

        return num_island

    def bfs(self, i: int, j: int, grid, visited) -> int:
        # possible moves
        i_step = [0, 1, 0, -1]
        j_step = [1, 0, -1, 0]

        # add first coordinate to queue and marked as visited
        queue = deque([(i, j)])
        visited[i][j] = True

        while len(queue) > 0:
            i, j = queue.popleft()
            # explore 4 directions
            for k in range(4):
                i_next = i + i_step[k]
                j_next = j + j_step[k]
                # check if steps in boundaries
                if 0 <= i_next < len(grid) and 0 <= j_next < len(grid[0]):
                    # check if we found another 1, and if its not explored
                    if grid[i_next][j_next] == '1' and visited[i_next][j_next] == False:
                        queue.append((i_next, j_next))
                        visited[i_next][j_next] = True
        return 1
