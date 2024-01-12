
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        len_dict = len(nums)+1
        i, j, total = 0, 0, nums[0]
        n = len_dict-1
        while i<n:
            if nums[j-1]>=target:
                return 1
            if total<target:
                if j<n-1:
                    j+=1
                    total += nums[j]
                    continue
                    
                else:
                    break
            elif total>=target:
                len_dict = min(len_dict,j-i+1)
                total -= nums[i]
                i+=1
                continue
            
        return len_dict if len_dict<n+1 else 0
