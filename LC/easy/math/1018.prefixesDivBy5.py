class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res =[]
        temp = 0
        for num in nums:
            temp = (temp << 1) + num
            res.append(temp%5 == 0)
        return res

