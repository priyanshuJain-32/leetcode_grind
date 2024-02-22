class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # My approach
        total = 0
        def inorder(root):
            if not root:
                return []
            nonlocal total
            left = inorder(root.left)
            total += root.val
            right = inorder(root.right)
            return left + [root] + right
        tree = inorder(root)
        lag = 0
        for i in tree:
            temp = i.val
            i.val = total - lag
            lag += temp
        return root