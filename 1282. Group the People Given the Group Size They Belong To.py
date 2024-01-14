class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_dict = defaultdict(list)
        for i in range(len(groupSizes)):
            group_dict[groupSizes[i]].append(i)
        ret = []
        for k,v in group_dict.items():
            if k<len(v):
                for i in range(0,len(v), k):
                    ret.append(v[i:i+k])
                continue
            ret.append(v)
        return ret
