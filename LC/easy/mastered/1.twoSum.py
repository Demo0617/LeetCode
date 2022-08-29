class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hasphasp = {}
        for ind, num in enumerate(nums):
            hasphasp[num] = ind

        for ind, num in enumerate(nums):
            if (target - num) in hasphasp.keys():
                if hasphasp[target - num] != ind:
                    return [ind, hasphasp[target - num]]