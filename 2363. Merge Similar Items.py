class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        self.d = defaultdict(int)
        def traverse(item):
            for a,b in item:
                self.d[a]+=b
        traverse(items1)
        traverse(items2)
        ans = []
        for k in sorted(self.d.keys()):
            ans.append([k,self.d[k]])
        return ans