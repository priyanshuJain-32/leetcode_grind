class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafs1 = []
        def leafs(root):
            if not root:
                return []
            if not root.left and not root.right:
                leafs1.append(root.val)
            leafs(root.left)
            leafs(root.right)
        leafs(root1)
        leafs2 = leafs1.copy()
        leafs1 = []
        leafs(root2)
        return leafs1==leafs2