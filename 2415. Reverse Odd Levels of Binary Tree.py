class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Another Iterative solution
        # queue = deque()
        # queue.append(root)
        # depth = 1
        # while queue:
        #     if depth%2==0:
        #         l = 0
        #         r = len(queue)-1
        #         while l<r:
        #             queue[l].val,queue[r].val = queue[r].val,queue[l].val
        #             l+=1
        #             r-=1
            
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #             queue.append(node.right)
        #     depth+=1
        # return root

        # My recursive approach
        def traverse(root,depth):
            if not root:
                return
            if not root.left:
                return root
            if depth%2==0:
                root.left.val, root.right.val = root.right.val, root.left.val
            root.right = traverse(root.right,depth+1)
            root.left = traverse(root.left,depth+1)
            return root
        return traverse(root,0)
        