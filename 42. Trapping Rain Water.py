class Solution:
    def trap(self, height: List[int]) -> int:
        i = 1
        j = len(height)-1
        if j-1<=0:
            return 0
        lmax = height[0]
        rmax = height[-1]
        ans = 0
        while i<=j:
            if lmax<height[i]:
                lmax = height[i]
            if rmax<height[j]:
                rmax = height[j]
            
            if lmax<=rmax:
                ans += lmax - height[i]
                i+=1
            else:
                ans += rmax - height[j]
                j-=1
        return ans


    # def trap(self, height: List[int]) -> int:
    #     return self.helper(height)
    # def helper(self,height):
    #     i,j = 0,0
    #     n = len(height)
    #     water = 0
    #     while i<len(height)-1:
    #         if height[i]>0:
    #             j = i+1
    #             while j<n and height[j]<height[i]:
    #                 j+=1
    #             if j==n: # if we don't find the j
    #                 height[i]=max(height[i+1:])
    #                 j=i
    #                 continue
    #             else:
    #                 k = i
    #                 while k<j:
    #                     water+=height[i]-height[k]
    #                     k+=1
    #                 i=j
    #         else:
    #             i+=1
    #             continue
                
    #     return water
        # keep i and j
        # if i is at a non-zero:
            # mark_container start
            # start from i+1 and find a j which is equal or more than i
                # if j is not found increment i to next non-zero i
                # else:
                    # now from i increment and keep saving the water value
                # after reaching the j increment j again and find the next i

        # 0,1,1,3,4,4,5,8,10,11,13,14

        # 3,3,2,2

        # 2,3,3,4,7
        # 7,5,4,4,3
        # 2,1,0