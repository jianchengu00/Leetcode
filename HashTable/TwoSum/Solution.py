class Solution:
    def two_sum(self, nums: list, target: int):
        # indices to return
        idx = []

        # create dictionary
        num_dict = {num: i for i, num in enumerate(nums)}

        # main loop
        for i, num in enumerate(nums):
            if target - num in num_dict and num_dict[target - num] != i:
                idx.append(i)
                idx.append(num_dict[target - num])
                return idx
