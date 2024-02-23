class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left, root.right = right, left
        return root