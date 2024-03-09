class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        UAM = [0]*k
        user = {}
        for i,j in logs:
            if i not in user:
                user[i] = {j}
            else:
                user[i].add(j)
        for v in user.values():
            n = len(v)
            if n==0:
                continue
            UAM[n-1] += 1
        return UAM