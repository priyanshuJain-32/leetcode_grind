class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.d = defaultdict(int)
        def traverse(root,depth):
            if not root:
                return
            self.d[depth]+=root.val
            traverse(root.left,depth+1)
            traverse(root.right,depth+1)
        traverse(root,1)
        self.d = [(k,v) for k,v in self.d.items()]
        self.d.sort(key=lambda x: x[1], reverse=True)
        return self.d[0][0]