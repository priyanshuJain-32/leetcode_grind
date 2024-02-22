class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev, res = None, 100001
        def inorder(root):
            if not root:
                return
            nonlocal prev, res
            inorder(root.left)
            if prev:
                res = min(res, abs(root.val - prev.val))
            prev = root
            inorder(root.right)
        inorder(root)
        return res