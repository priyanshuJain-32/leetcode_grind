class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total = 0

        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            self.total += abs(left-right)
            return left+right+root.val
            
        helper(root)
        
        return self.total