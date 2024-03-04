class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = defaultdict(list)
        def traverse(root, depth):
            if not root:
                return
            self.ans[depth].append(root.val)
            traverse(root.left, depth + 1)
            traverse(root.right, depth + 1)
        traverse(root, 0)
        ret = []
        dir = 1
        for i in self.ans.keys():
            ret.append(self.ans[i][::dir])
            dir *=-1
        return ret