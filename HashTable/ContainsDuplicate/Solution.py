class Solution:
    def contains_duplicate(self, nums: list) -> bool:
        item_dict = {}
        for n in nums:
            if n in item_dict:
                return True
            item_dict[n] = 1
        return False
