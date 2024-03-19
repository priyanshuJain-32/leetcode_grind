class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        arro = [i for i in nums if i%2]
        arre = [i for i in nums if not i%2]
        ans = []
        for i,j in zip(arre, arro):
            ans.append(i)
            ans.append(j)
        return ans