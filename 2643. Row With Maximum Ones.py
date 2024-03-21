class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [0,0]
        for i in range(len(mat)):
            c = mat[i].count(1)
            if c>ans[1]:
                ans[0] = i
                ans[1] = c
        return ans