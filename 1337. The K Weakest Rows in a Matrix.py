class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        l = [(sum(v),i) for i,v in enumerate(mat)]
        return [v for k,v in sorted(l)[:k]]