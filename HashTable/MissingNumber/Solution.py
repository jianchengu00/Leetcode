class Solution:
    def missing_number(self, nums: list) -> int:
        ordered_nums = [i for i in range(len(nums) + 1)]
        nums_dict = {n: 1 for n in nums}

        for n in ordered_nums:
            if n not in nums_dict:
                return n
