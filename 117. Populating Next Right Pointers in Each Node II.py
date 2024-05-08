"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self.depth = defaultdict(list)
        def travel(root,depth):
            if not root:
                return
            self.depth[depth].append(root)
            travel(root.left,depth+1)
            travel(root.right,depth+1)
        travel(root,1)
        for k,v in self.depth.items():
            n = len(v)
            if n>1:
                for i in range(n-1):
                    v[i].next = v[i+1]
                v[n-1].next = None
        return root