class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 1:
            return 1 if nums[0] != val else 0

        i, j = 0, 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i