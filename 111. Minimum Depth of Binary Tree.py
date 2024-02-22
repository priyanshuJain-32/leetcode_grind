class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.minDepth(root.left) + 1
        right = self.minDepth(root.right) + 1

        if not (root.left or root.right):
            return 1
        
        if root.left is None:
            return right
        
        if root.right is None:
            return left
        
        return min(left, right)