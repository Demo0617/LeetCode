class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums.sort()
        n = len(nums)
        start = 0
        res = []
        while start < n:
            end = start
            while end + 1 < n and nums[end + 1] == nums[end] + 1:
                end += 1
            if start == end:
                res.append(str(nums[start]))
            else:
                res.append('{}->{}'.format(str(nums[start]),str(nums[end])))
            start = end + 1
        return res
