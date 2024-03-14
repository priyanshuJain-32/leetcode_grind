class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # n = len(nums)
        countmap = defaultdict(int)
        countmap[0] = 1
        curr_s = 0
        total_s = 0
        
        for n in nums:
            curr_s += n
            if curr_s - goal in countmap:
                total_s += countmap[curr_s-goal]
            countmap[curr_s] += 1
        return total_s

        # if n==1:
        #     return 1 if nums[0]==goal else 0
        # i = 0
        # j = 0
        # prefix = [0]*(n+1)
        # while j<n:
        #     prefix[j+1] = prefix[j] + nums[j]
        #     j+=1
        # cnt = 0
        # i = 0
        # while i<n:
        #     for j in range(i+1,n+1):
        #         if prefix[j]==goal:
        #             cnt += 1
        #         prefix[j]-= nums[i]
        #     i+=1
        #     if prefix[-1]<goal:
        #         break
        # return cnt
        # countmap = defaultdict(int)
        # j = 1
        # diff = 0
        # while i<n and j<n:
        #     if prefix[j]-diff==goal:
        #         countmap[i] += 1
        #     elif prefix[j]-diff>goal:
        #         diff+=nums[i]
        #         j=i
        #         i += 1
        #     j+=1
        # print(countmap)
        # 1+2+2+3+3
        #     prefix[j+1] = prefix[j] + nums[j]
        #     j += 1
        #     print(prefix)
        # print(countmap)
        # return 0
        # i = 0
        # j = 1
        # cnt = 0
        # total = nums[i]
        # while i<j and j<n:
        #     if total==goal:
        #         cnt += 1
        #         total += nums[j]
        #         j+=1
        #     elif total < goal:
        #         total += nums[j]
        #         j += 1
        #     elif total > goal:
        #         total -= nums[i]
        #         i += 1
        # return cnt
            

        
        # d = defaultdict(list)
        # cnt = 0
        # for i in range(max(goal,1),n+1): # [0,5]
        #     k = 0
        #     total = sum(nums[k:k+i])
        #     while k<=n-i: # [0,5]
        #         # print(total,nums[k:k+i])
        #         if total==goal: #
        #             # d[i].append(nums[k:k+i])
        #             cnt += 1
        #         if k==n-i:
        #             break
        #         total -= nums[k]
        #         total += nums[k+i]
        #         k+=1
                
        # # print(d)
        # return cnt