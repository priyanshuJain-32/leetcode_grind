class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1,1]
        if rowIndex==0:
            return [1]
        elif rowIndex==1:
            return [1,1]
        for i in range(2,rowIndex+1):
            temp = [1]
            for j in range(1,i):
                temp.append(ans[j-1]+ans[j])
            temp.append(1)
            ans = temp.copy()
        return ans