class Solution:
    def unique_paths(self, m: int, n: int) -> int:
        unique_paths = [[None for j in range(n)] for i in range(m)]
        return self.opt(m - 1, n - 1, unique_paths)

    def opt(self, i, j, unique_paths):
        # if out of bounds, return 0 for no path
        if i < 0 or j < 0:
            return 0
        # only 1 possible path from starting point to (0, 0)
        if i == 0 and j == 0:
            return 1
        # if already found num unique paths, then return it
        if unique_paths[i][j] is not None:
            return unique_paths[i][j]
        # only 2 possible spots before reaching (i, j), which simply extend their path
        # that means total num of unique paths to (i, j) is the sum of the
        # num of unique paths in its two prior spots
        unique_paths[i][j] = self.opt(i - 1, j, unique_paths) + self.opt(i, j - 1, unique_paths)
        return unique_paths[i][j]
