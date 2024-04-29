class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.L = defaultdict(list)
        self.count = 0
        def traverse(root,depth):
            if not root.left:
                return root
            if depth%2==1:
                self.L[depth].append(root.left)
                self.L[depth].append(root.right)
                self.count += 2
            root.left = traverse(root.left,depth+1)
            root.right = traverse(root.right,depth+1)
            return root
        root = traverse(root,1)
        for k,v in self.L.items():
            n = len(v)
            for i in range(n//2):
                v[i].val, v[n-i-1].val = v[n-i-1].val, v[i].val
        return root