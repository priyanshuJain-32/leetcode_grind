class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # My Approach

        satisfaction.sort()
        n = len(satisfaction)
        i = 0
        max_score = -1000000
        while i<n:
            score = 0
            count = 1
            for j in range(i,n):
                score += satisfaction[j]*count
                count += 1
            if score>max_score:
                max_score = score
            else:
                break
            i+=1
        return max(max_score, 0)

        # Some legend
        # a=sorted(satisfaction,reverse=True)
        # b,c= 0,0
        # for i in a:
        #     if(b+i>0):
        #         c+=b+i
        #         b+=i
        # return c