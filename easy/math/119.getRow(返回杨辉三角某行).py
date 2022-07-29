class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(1,rowIndex+1):
            res.append(1)
            start = 1
            end = i - 1
            if start > end: continue
            for j in range(end , start-1, -1):
                res[j] += res[j - 1]
        return res
