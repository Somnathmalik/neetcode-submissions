"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        ptrA, ptrB = p, q
        
        while ptrA != ptrB:
            # Move up to parent, or switch to the other node's start if root is reached
            ptrA = ptrA.parent if ptrA else q
            ptrB = ptrB.parent if ptrB else p
            
        return ptrA
