class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root] + inorder(root.right)
        nodes = inorder(root)
        for i in range(len(nodes)-1):
            nodes[i].left = None
            nodes[i].right = nodes[i+1]
        nodes[-1].left = None
        nodes[-1].right = None
        return nodes[0]