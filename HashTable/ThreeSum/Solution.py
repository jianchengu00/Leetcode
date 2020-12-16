class Solution:
    def three_sum(self, nums: list) -> list:
        # unique triplets
        unique_triplets = {}

        # index lookup for nums
        nums_dict = {n: i for i, n in enumerate(nums)}

        # duplicates for first to optimize speed
        first_dups = set()

        for i in range(len(nums)):
            if nums[i] not in first_dups:
                first = nums[i]
                first_dups.add(first)
                # find a pair of numbers whose sum == -nums[i]
                for j in range(i + 1, len(nums)):
                    # fix second number
                    second = nums[j]
                    # check if the third number to make 0 sum exists, and if it's unique
                    third = 0 - first - second
                    if third in nums_dict and nums_dict[third] != j and nums_dict[third] != i:
                        # create a sorted list of the potential nums
                        triplet = sorted([first, second, third])
                        if str(triplet) not in unique_triplets:
                            unique_triplets[str(triplet)] = triplet
        return [unique_triplets[key] for key in unique_triplets]
