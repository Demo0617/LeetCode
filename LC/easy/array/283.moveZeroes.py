class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p, q = 0, 0
        while q < len(nums):
            if nums[q] != 0:
                nums[p] = nums[q]
                p += 1
            q += 1
        while p < len(nums):
            nums[p] = 0
            p += 1