class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        def traverse(root,path, total, targetSum):
            if root:
                path.append(root.val)
                total += root.val
                if not root.left and not root.right and total==targetSum:
                    self.ans.append(path)
                traverse(root.left,path.copy(),total,targetSum)
                traverse(root.right,path.copy(),total,targetSum)
        traverse(root,[],0,targetSum)
        
        return self.ans