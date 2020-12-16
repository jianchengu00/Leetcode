import sys


class Solution:
    def max_sub_array(self, nums: list) -> int:
        local_max = 0
        global_max = -sys.maxsize

        for n in nums:
            local_max = max(n, n + local_max)
            if local_max > global_max:
                global_max = local_max

        return global_max
