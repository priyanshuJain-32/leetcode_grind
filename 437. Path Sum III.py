class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # In this question we will look at the sum of 
        # left branch onwards
        # right branch onwards
        # sum including root
        # https://www.youtube.com/watch?v=uZzvivFkgtM&t=2s
        
        self.counts = defaultdict(int)
        self.counts[0] = 1
        self.ans = 0
        
        def travel(root,curr):
            
            if not root:
                return
            
            curr = curr+root.val

            if curr-targetSum in self.counts:
                self.ans += self.counts[curr-targetSum]
            
            self.counts[curr] += 1
            
            travel(root.left,curr)
            travel(root.right,curr)

            self.counts[curr] -= 1
        travel(root,0)
        return self.ans

        # self.ans = 0
        # def travel(root,Sum,freshStart):
        #     if not root:
        #         return
        #     S = Sum-root.val
        #     if S==0:
        #         self.ans += 1
        #     if freshStart:
        #         travel(root.left,Sum,True)
        #         travel(root.right,Sum,True)
        #     travel(root.left,Sum-root.val,False)
        #     travel(root.right,Sum-root.val,False)
        # travel(root,targetSum,True)
        # return self.ans