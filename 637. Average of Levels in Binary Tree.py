class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avg_cnt = defaultdict(int)
        avg_of = defaultdict(int)
        def averages(root, level):
            if root:
                avg_of[level] += root.val
                avg_cnt[level] += 1
                averages(root.left, level+1)
                averages(root.right, level+1)
        averages(root, 0)
        return [avg_of[i]/avg_cnt[i] for i in range(len(avg_cnt))]