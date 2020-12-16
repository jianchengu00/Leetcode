class Solution:
    def search(self, nums: list, target: int) -> int:
        pivot = self.find_pivot(nums, 0, len(nums) - 1)

        # If we didn't find a pivot,
        # then nums is not rotated at all
        if pivot == -1:
            return self.binary_search(nums, 0, len(nums) - 1, target)

        # If we found a pivot, then first
        # compare with pivot and then
        # search in two subarrays around pivot
        if nums[pivot] == target:
            return pivot
        if nums[0] <= target:
            return self.binary_search(nums, 0, pivot - 1, target)
        return self.binary_search(nums, pivot + 1, len(nums) - 1, target)

    def find_pivot(self, arr, low, high) -> int:
        if high < low:
            return -1
        if high == low:
            return low

        # calculate middle
        mid = (high + low) // 2

        if mid < high and arr[mid] > arr[mid + 1]:
            return mid
        if mid > low and arr[mid] < arr[mid - 1]:
            return mid - 1
        if arr[low] >= arr[mid]:
            return self.find_pivot(arr, low, mid - 1)

        return self.find_pivot(arr, mid + 1, high)

    def binary_search(self, arr, low, high, target):
        if high < low:
            return -1

        # calculate middle
        mid = (high + low) // 2

        if target == arr[mid]:
            return mid
        if target > arr[mid]:
            return self.binary_search(arr, (mid + 1), high, target)
        return self.binary_search(arr, low, (mid - 1), target)
