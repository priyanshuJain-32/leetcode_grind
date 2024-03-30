class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums)
        n = len(nums)
        i,j = 0,0
        cnt = 0
        sub_cnt = 0
        while j<n:
            if nums[j]==m:
                cnt += 1
            while cnt>=k:
                if nums[i]==m:
                    cnt -=1
                i+=1
            sub_cnt += i
            j+=1
        return sub_cnt