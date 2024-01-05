# My naive approach
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def bsearch(L,k):
            left = 0
            right = len(L)-1
            mid = 0   

            while left<=right:
                mid = (left+right)//2
                if L[mid]>k:
                    right = mid-1
                    
                elif L[mid]<k:
                    left = mid+1
                else:
                    return mid
            return -1
        
        i = 0
        L = [0,0]
        while i<len(numbers)-1:
            L[0] = i+1
            idx = bsearch(numbers[i+1:],target-numbers[i])
            if idx != -1:
                L[-1] = idx+1+L[0]
                return L
            else:
                i += 1

# Shorter approach
        low, high = 0, len(numbers)-1
                c_sum = 0
                while low<=high:
                    c_sum = numbers[low]+numbers[high]
                    if c_sum==target:
                        return [low+1,high+1]
                    elif c_sum<target:
                        low += 1
                        continue
                    else:
                        high-=1
                        continue
