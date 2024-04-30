class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        self.pointers = defaultdict()
        self.childs = set()
        for n,c,l in descriptions:
            self.childs.add(c)
            if n in self.pointers:
                node = self.pointers[n]
            else:
                node = TreeNode(n)
            if c in self.pointers:
                if l==1:
                    node.left = self.pointers[c]
                    self.pointers[c] = node.left
                else:
                    node.right = self.pointers[c]
                    self.pointers[c] = node.right
            else:
                if l==1:
                    node.left = TreeNode(c)
                    self.pointers[c] = node.left
                else:
                    node.right = TreeNode(c)
                    self.pointers[c] = node.right
            self.pointers[n] = node
        
        return self.pointers[(self.parents-self.childs).pop()]