# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.pointers = defaultdict(TreeNode)
        self.paths = []
        self.max_depth = 0
        def traverse(root,depth,path):
            if not root:
                return ''
            path += str(root.val)+','
            self.pointers[root.val] = root
            if not root.left and not root.right:
                self.paths.append(path[:-1])
                self.max_depth = max(depth,self.max_depth)
            traverse(root.left,depth+1,path)
            traverse(root.right,depth+1,path)
        traverse(root,1,'')
        self.inspect = []
        
        for path in self.paths:
            path = path.split(',')
            if len(path)==self.max_depth:
                self.inspect.append(path)
        
        i = -1
        while self.inspect[0][i]!=self.inspect[-1][i]:
            i-=1
        return self.pointers[int(self.inspect[0][I])]