class Solution:
    def __init__(self):
        self.output = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return
        
        self.inorderTraversal(root.left)
        self.output.append(root.val)
        self.inorderTraversal(root.right)
        return self.output