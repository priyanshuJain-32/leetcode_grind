class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            return max(height(root.left)+1, height(root.right)+1)
        if not root:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and -2<height(root.left)-height(root.right)<2