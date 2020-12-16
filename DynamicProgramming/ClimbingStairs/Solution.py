class Solution:
    def climb_stairs(self, n: int) -> int:
        distinct_ways = [-1 for i in range(n)]
        return self.opt(distinct_ways, n)

    def opt(self, distinct_ways: list, current_step: int) -> int:
        # base cases
        if current_step == 1:
            return 1
        if current_step == 2:
            return 2
        if distinct_ways[current_step - 1] != -1:
            return distinct_ways[current_step - 1]

        # optimal subproblem relation
        distinct_ways[current_step - 1] = self.opt(distinct_ways, current_step - 1) + self.opt(distinct_ways,
                                                                                               current_step - 2)

        return distinct_ways[current_step - 1]
