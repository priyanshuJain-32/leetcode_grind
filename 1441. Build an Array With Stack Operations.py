class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i = 0
        k = 1
        ans = []
        while i<len(target):
            if target[i]==k:
                ans.append("Push")
                i+=1
                k+=1
                continue
            ans.extend(["Push","Pop"])
            k+=1
        return ans