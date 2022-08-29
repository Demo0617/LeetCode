class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0: return 0

        dp = [ 0 for i in range(l)]
        dp[0] = nums[0]
        for i in range(1, l):
            dp[i] = nums[i] + dp[i - 1] if dp[i - 1] > 0 else nums[i]

        return max(dp)
