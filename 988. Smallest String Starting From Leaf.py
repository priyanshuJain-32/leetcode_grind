class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.paths = []
        def traverse(root,path):
            if not root:
                return ""
            path += chr(97+root.val)
            if not root.left and not root.right:
                self.paths.append(path[::-1])
            traverse(root.left,path)
            traverse(root.right,path)
        traverse(root,"")
        return sorted(self.paths)[0]