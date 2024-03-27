n = len(nums)
        d = defaultdict(int)
        for i in nums:
            for j in i:
                d[j]+=1
        ans = []
        for k,v in d.items():
            if v==n:
                ans.append(k)
        return sorted(ans)