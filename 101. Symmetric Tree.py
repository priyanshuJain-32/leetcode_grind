class Solution:
    def sameTree(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not right and not left:
            return True
        elif not (right and left):
            return False
        return self.sameTree(left.left, right.right) and self.sameTree(left.right, right.left) and (left.val == right.val)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return
        return self.sameTree(root.left, root.right)