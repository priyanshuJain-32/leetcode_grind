class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # My second solution
        self.max_len = 0
        def traverse(root):
            if not root:
                return TreeNode(0)
            if not root.left and not root.right:
                root.val = 1
                return root
            left = traverse(root.left).val + 1
            right = traverse(root.right).val + 1
            root.val = max(left, right)
            self.max_len = max(left+right-2, self.max_len)
            return root
        traverse(root)
        return self.max_len

        # First slow approach
        # if not root:
        #     return 0
        # def traverse(root):
        #     if not root:
        #         return 0
        #     left = traverse(root.left) + 1
        #     right = traverse(root.right) + 1
        #     return max(left, right)
        # left = traverse(root.left)
        # right = traverse(root.right)

        # return max(left+right, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))