class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count = 0
        for i in nums:
            if i<target:
                count += 1
        ans = []
        for i in nums:
            if i==target:
                ans.append(count)
                count+=1
        return ans