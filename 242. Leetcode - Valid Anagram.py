class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Short approach
        return sorted(s)==sorted(t)

        # Longer approach
        # wordCount = {}
        # for i in s:
        #     if i in wordCount:
        #         wordCount[i]+=1
        #         continue
        #     wordCount[i]=1
        # try:
        #     for j in t:
        #         wordCount[j]-=1
        #     for i in wordCount.values():
        #         if i!=0:
        #             return False
        #     return True
        # except:
        #     return False
