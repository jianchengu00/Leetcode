class Solution:
    def can_jump(self, nums: list) -> bool:
        jumpable = [None for n in nums]
        return self.opt(len(nums) - 1, nums, jumpable)

    def opt(self, idx, nums, jumpable):
        if idx == 0:
            return True
        if jumpable[idx] is not None:
            return jumpable[idx]
        # The recurrence relation checks if each "possible" prior index
        # can successfully jump to this current index from the beginning
        for i in range(idx - 1, -1, -1):
            # Every "possible" prior index to try is an index who is within range
            # of our current index from their potential jumping distance
            if i + nums[i] >= idx:
                if self.opt(i, nums, jumpable):
                    jumpable[idx] = True
                    return jumpable[idx]
        jumpable[idx] = False
        return jumpable[idx]
