class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: return
        if m == 0:
            nums1[:] = nums2[:]
            return

        i = m - 1
        j = n - 1
        for k in range(m + n - 1, -1, -1):
            if nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
                if j == -1:
                    break
            else:
                nums1[k] = nums1[i]
                i -= 1
                if i == -1:
                    k -= 1
                    while k >= 0:
                        nums1[k] = nums2[j]
                        j -= 1
                        k -= 1
                    break

