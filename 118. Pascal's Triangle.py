class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1],[1,1]]
        if numRows<3:
            return ans[:numRows]
        for i in range(2,numRows):
            ans.append([1])
            for j in range(1,i):
                res = ans[i-1][j-1]+ans[i-1][j]
                ans[i].append(res)
            ans[i].append(1)
        return ans