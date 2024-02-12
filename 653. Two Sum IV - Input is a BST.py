class Solution:
    def __init__(self):
        self.seenCompliment = set()

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        if root.val in self.seenCompliment:
            return True
        self.seenCompliment.add(k-root.val)
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)