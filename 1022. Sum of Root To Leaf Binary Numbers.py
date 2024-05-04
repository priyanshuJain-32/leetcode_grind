class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        def sRTL(root, path):
            if not root:
                return 0
            path = (path<<1) + root.val
            sRTL(root.left, path)
            if not (root.left or root.right):
                self.total += path
            sRTL(root.right, path)
        sRTL(root, 0)
        return self.total
