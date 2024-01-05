class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i,j in enumerate(citations):
            if i>=j:
                return i
        return i+1
        
        # Wrong approach
        # d = {i:0 for i in citations}
        # n = len(citations)
        # if n==1:
        #     return 0 if citations[0]==0 else 1
        # elif sum(citations)==0:
        #     return 0
        # elif n<min(citations):
        #     return n
        # for k in d.keys():
        #     for i in citations:
        #         if k<=i:
        #             d[k] += 1
        # for k,v in d.items():
        #     if k<=v:
        #         return k
        # return 1