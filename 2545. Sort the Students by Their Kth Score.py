class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        # Shorter way
        return sorted(score, key = lambda i: i[k], reverse=True)
        
        # My original way
        m = len(score)
        row_order = defaultdict(lambda: 0)
        
        col_scores = [0]*m
        for i in range(m):
            row_order[score[i][k]] = i
            col_scores[i] = score[i][k]
        
        col_scores.sort(reverse=True)
        
        ans = []
        for i in col_scores:
            ans.append(score[row_order[i]])
        return ans
