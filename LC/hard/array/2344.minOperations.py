class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        g = numsDivide[0]
        for num in numsDivide:
            g = gcd(g, num)
        for i, num in enumerate(sorted(nums)):
            if g % num == 0:
                return i
        return -1
