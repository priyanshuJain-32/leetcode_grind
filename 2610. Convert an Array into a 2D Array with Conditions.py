class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # Some Pro's solution
        ret = []
        while nums:
            s = set(nums)
            r = []
            for i in s:
                r.append(i)
                nums.remove(i)
            ret.append(r)
        return ret
        
        # My slow approach
        countDict = defaultdict()
        for i in nums:
            if i in countDict:
                countDict[i]+=1
                continue
            countDict[i] = 1
        ret = []
        while sum(countDict.values())!=0:
            keys = list(countDict.keys())
            ret.append(keys)
            for k in keys:
                countDict[k]-=1
                if countDict[k]==0:
                    del countDict[k]
        return ret
