class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        queue.append(root)
        root.val = 0
        toReplace = []
        while queue:
            total = 0
            toReplace = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                toReplace.append(curr)
                if curr.left:
                    queue.append(curr.left)
                    total += curr.left.val
                if curr.right:
                    queue.append(curr.right)
                    total += curr.right.val
            for node in toReplace:
                d = 0
                if node.left:
                    d += node.left.val
                if node.right:
                    d += node.right.val
                if node.left:
                    node.left.val = total - d
                if node.right:
                    node.right.val = total - d
        return root          