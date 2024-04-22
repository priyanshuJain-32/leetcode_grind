class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Faster solution but not fastest
        if not preorder or not inorder:
            return
        root = TreeNode(preorder[0])
        m = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:m+1],inorder[:m])
        root.right = self.buildTree(preorder[m+1:],inorder[m+1:])
        return root

        # # Slow approach
        # def add(root, val):
        #     if self.pos[root.val]<self.pos[val]:
        #         if root.right == None:
        #             root.right = TreeNode(val)
        #         else:
        #             root.right = add(root.right,val)
        #     elif self.pos[root.val]>self.pos[val]:
        #         if root.left == None:
        #             root.left = TreeNode(val)
        #         else:
        #             root.left = add(root.left,val)
        #     return root
        # for num in preorder[1:]:
        #     root = add(root,num)
        # return root