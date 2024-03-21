class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0
        for i in range(len(strs[0])):
            temp = ""
            for j in range(len(strs)):
                temp+=strs[j][i]
            if list(temp)!=sorted(temp):
                cnt += 1
        return cnt