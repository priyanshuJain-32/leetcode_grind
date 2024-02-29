class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        def traverse(root):
            if not root:
                return 0
            traverse(root.left)
            if root.left:
                if not root.left.left and not root.left.right:
                    self.total += root.left.val
            traverse(root.right)
        traverse(root)
        return self.total