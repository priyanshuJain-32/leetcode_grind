class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        seen = set()
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j, k = i+1, n-1
            residual = 0-nums[i]
            while j<k:
                if nums[j]+nums[k]>residual:
                    k-=1
                elif nums[j]+nums[k]<residual:
                    j+=1
                else:
                    seen.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k = n-1
            # i+=1
        
        return [list(i) for i in seen]
        
        
        
        # def bsearch(L, k):
        #     left = 0
        #     right = len(L)-1
        #     mid = 0
        #     while left<=right:
        #         mid = (left+right)//2
        #         if L[mid]<k:
        #             left = mid+1
        #         elif L[mid]>k:
        #             right = mid-1
        #         else:
        #             return mid, True
        #     return left, False
        # nums.sort()
        # if nums[-1]<0:
        #     return []
        # triplets = list()
        # seen = set()
        # n = len(nums)
        # center,status = bsearch(nums,0)
        # i = 0
        # # print(nums,center)
        # while i<=center:
        #     if nums[i]>0:
        #         break
        #     k = n-1
        #     j,status = bsearch(nums[i+1:k], 0-nums[i]-nums[k])
        #     j += i+1
        #     while k>=center:
        #         if status==True and k!=j and j!=i:
        #             # seen.add(tuple(sorted([nums[i],nums[k],nums[j]])))
        #             seen.add((nums[i],nums[k],nums[j]))
        #         k-=1
        #         j, status=bsearch(nums[i+1:k], 0-nums[i]-nums[k])
        #         j+= i+1
        #     i+=1
        # print(seen)
        # # if center>n//2:
        # # while i>-1 and j<len(nums):

        
        # # print(i,j)
        
        # return [list(i) for i in seen]