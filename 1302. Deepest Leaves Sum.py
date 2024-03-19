class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.max_depth = 0
        def isleaf(root):
            return not (root.left or root.right)
        def depth(root, d):
            if not root:
                return 0
            if isleaf(root) and d>self.max_depth:
                self.ans = 0
                self.max_depth=d
            if isleaf(root) and d==self.max_depth:
                self.ans += root.val
            depth(root.left, d+1)
            depth(root.right, d+1)
        depth(root,0)
        return self.ans