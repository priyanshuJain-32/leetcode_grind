class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def prune(root):
            if not root:
                return None
            root.left = prune(root.left)
            root.right = prune(root.right)
            if (not root.left) and (not root.right) and (root.val==0):
                return None
            return root
        return prune(root)