class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        i, j = 0, 1
        while j < len(nums) - 1:
            if nums[i] != nums[j]:
                return nums[i]
            i += 2
            j += 2

        return nums[-1]

