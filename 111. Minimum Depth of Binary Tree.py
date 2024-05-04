class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.depths = []
        def travel(root,depth):
            if not root:
                return 0
            if not root.left and not root.right:
                self.depths.append(depth)
            travel(root.left,depth+1)
            travel(root.right,depth+1)
        travel(root,1)
        return min(self.depths)