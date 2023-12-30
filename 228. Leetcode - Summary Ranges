class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        ret = []
        count = 1
        n = len(nums)
        if n==1:
            return [str(nums[0])]
        while i<n-1:
            if nums[i]==nums[i+1]-1:
                count += 1
                if i==n-2:
                    ret.append(str(nums[i-count+2]) + "->" + str(nums[i+1]))
                    break
            elif count==1:
                ret.append(str(nums[i]))
            else:
                ret.append(str(nums[i-count+1]) + "->" + str(nums[i]))
                count = 1
            i+=1
            if i==n-1:
                ret.append(str(nums[i]))
        return ret
