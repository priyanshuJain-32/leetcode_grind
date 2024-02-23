class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        L = []
        def inorder(root):
            if not root:
                return []
            nonlocal L
            inorder(root.left)
            L.append(root.val)
            inorder(root.right)
        inorder(root1)
        inorder(root2)
        return sorted(L)