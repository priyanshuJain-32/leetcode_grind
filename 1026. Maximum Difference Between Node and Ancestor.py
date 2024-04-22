class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # def traverse(root,curr_max,curr_min):
        #     if not root:
        #         return curr_max-curr_min
        #     curr_max = max(curr_max,root.val)
        #     curr_min = min(curr_min,root.val)
        #     return max(traverse(root.left,curr_max,curr_min),traverse(root.right,curr_max,curr_min))
        # return traverse(root,-float('inf'),float('inf'))        
        
        self.paths = []
        def traverse(root,path):
            if not root:
                return ''
            path += str(root.val)+','
            if not root.left and not root.right:
                self.paths.append(path[:-1])
                
            traverse(root.left,path)
            traverse(root.right,path)
        traverse(root,'')
        
        max_diff = 0
        for path in self.paths:
            path = list(map(int,path.split(",")))
            d = max(path)-min(path)
            if d>max_diff:
                max_diff = d
        return max_diff