class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        que = collections.deque()
        for i in range(k):
            while que and que[-1] < nums[i]:
                que.pop()
            que.append(nums[i])
        ans.append(que[0])

        for i in range(k,len(nums)):
            if nums[i-k] == que[0]:
                que.popleft()
            while que and que[-1] < nums[i]:
                que.pop()
            que.append(nums[i])
            ans.append(que[0])
        return ans
