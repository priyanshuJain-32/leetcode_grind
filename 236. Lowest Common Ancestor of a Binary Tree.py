class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Faster community solution
        
        if not root or p==root or q==root:
            return root

        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r: # We found both p and q on left and right
            return root
        return l or r
        
        
        # My Solution
        self.ancestors = {root.val:None}
        
        def traverse(root, parent):
            if not root:
                return
            self.ancestors[root.val] = parent
            parent = root.val
            
            traverse(root.left,parent)
            traverse(root.right, parent)
        traverse(root.left, root.val)
        traverse(root.right, root.val)
        
        parents_p = [p.val]
        parents_q = {q.val}
        
        parent = self.ancestors[p.val]
        while parent!=None:
            parents_p.append(parent)
            parent = self.ancestors[parent]
        
        parent = self.ancestors[q.val]
        while parent!=None:
            parents_q.add(parent)
            parent = self.ancestors[parent]
        

        for i in parents_p:
            if i in parents_q:
                return ListNode(i)