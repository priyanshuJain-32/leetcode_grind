class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        Nums = nums*2
        self.d = defaultdict(deque)
        stack = []
        i = 0
        while i<len(Nums):
            if stack and stack[-1]<Nums[i]:
                self.d[stack[-1]].append(Nums[i])
                stack.pop()
            else:
                stack.append(Nums[i])
                i+=1
        for i in stack:
            if i not in self.d:
                self.d[i].append(-1)
        ans = []
        for i in nums:
            if self.d[i]:
                ans.append(self.d[i].popleft())
            else:
                ans.append(-1)
        return ans