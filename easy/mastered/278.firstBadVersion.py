# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                else:
                    r = mid - 1
            elif isBadVersion(mid + 1):
                return mid + 1
            else:
                l = mid + 1