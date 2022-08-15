class NumArray:

    def __init__(self, nums: List[int]):
        self.pre_sums = [0]

        for num in nums:
            self.pre_sums.append(num + self.pre_sums[-1])


    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sums[right + 1] - self.pre_sums[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)