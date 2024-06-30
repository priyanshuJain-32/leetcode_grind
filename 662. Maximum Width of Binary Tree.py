class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = defaultdict(list)

        def travel(root, depth, index):
            if not root:
                
                return
            self.d[depth].append(index)
            travel(root.left, depth+1, 2*index)
            travel(root.right, depth+1, 2*index+1)
        
        travel(root, 0, 0)
        
        max_w = 0
        for value in self.d.values():
            if len(value)>1:
                max_w = max(max_w, value[-1]-value[0]+1)
            else:
                max_w = max(max_w, 1)
        
        return max_w
