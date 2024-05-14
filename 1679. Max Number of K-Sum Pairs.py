class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # counts = defaultdict(int)
        # for n in nums:
        #     counts[n] += 1
        # ops = 0
    
        # for n in nums:
    
        #     if k-n in counts:
        #         if k-n==n and counts[n]>1:
        #             ops += 1
        #             counts[n] -= 2
        #             continue
        #         elif k-n==n and counts[n]<=1:
        #             continue
        #         tOps = min(counts[n],counts[k-n])
        #         counts[n]-= tOps
        #         counts[k-n]-= tOps
        #         ops+=tOps
        
        # return ops
        
        # Fast and simple
        i,j = 0,len(nums)-1
        nums.sort()
        ops = 0
        while i<j:
            temp = nums[i]+nums[j]
            if temp==k:
                ops+=1
                i+=1
                j-=1
            elif temp>k:
                j-=1
            else:
                i+=1
        return ops