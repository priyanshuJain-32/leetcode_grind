class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # Smarter approach
        total = 0
        def inorder(root):
            if not root:
                return
            nonlocal total
            inorder(root.right)
            total += root.val
            root.val = total
            inorder(root.left)
        inorder(root)
        return root


        # My approach won
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