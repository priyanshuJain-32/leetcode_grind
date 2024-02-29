class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def identical(root1, root2):
            if not root1 and not root2:
                return True
            if not (root1 and root2):
                return False
            if root1.val==root2.val:
                return identical(root1.left, root2.left) and identical(root1.right, root2.right)
            return False
        
        que = deque()
        que.append(root)
        i = 0
        while que:
            i+=1
            node = que.popleft()
            if identical(node, subRoot):
                return True
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        return False