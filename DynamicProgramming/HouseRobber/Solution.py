class Solution:
    def rob(self, nums: list) -> int:
        max_values = [-1 for n in nums]
        return self.opt(max_values, nums, len(nums) - 1)

    def opt(self, max_values: list, nums, house_num: int) -> int:
        # base cases
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if house_num < 0:
            return 0
        if max_values[house_num] != -1:
            return max_values[house_num]

        max_values[house_num] = max(nums[house_num] + self.opt(max_values, nums, house_num - 2),
                                    self.opt(max_values, nums, house_num - 1))
        return max_values[house_num]
