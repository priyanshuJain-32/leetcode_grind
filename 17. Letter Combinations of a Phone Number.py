class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        D = {
            "2":["abc",3],
            "3":["def",3],
            "4":["ghi",3],
            "5":["jkl",3],
            "6":["mno",3],
            "7":["pqrs",4],
            "8":["tuv",3],
            "9":["wxyz",4]
        }
        ans = [""]
        for i in digits:
            ans *= D[i][1]
            ans.sort()
            k = 0
            for j in range(len(ans)):
                ans[j]+=D[i][0][k]
                k+=1
                if k==len(D[i][0]):
                    k=0
        return ans