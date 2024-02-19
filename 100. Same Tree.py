class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and q:
            return False
        if not q and p:
            return False
        if not p and not q:
            return True
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and (p.val == q.val)