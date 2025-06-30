"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        h = {}
        if not node: return None

        h[node] = Node(node.val)
        st = [node]
        seen = set()
        seen.add(node)
        while st:
            new_node = st.pop()
            for nei in new_node.neighbors:
                if nei not in seen:
                    seen.add(nei)
                    st.append(nei)
                    h[nei] = Node(nei.val)
        
        for old,new in h.items():
            for nei in old.neighbors:
                new.neighbors.append(h[nei])
        
        return h[node]

        # TC : O(V+E)
        # SC : O(V)