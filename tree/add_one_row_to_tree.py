# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if not root:
            return 
        if depth == 1:
            newRoot = TreeNode(val,left=root)
            root = newRoot
        if depth == 2:
            tempL = root.left
            tempR = root.right
            nodeL = TreeNode(val,left=tempL)
            nodeR = TreeNode(val,right=tempR)
            root.left = nodeL
            root.right = nodeR
        else:
            self.addOneRow(root.left,val,depth-1)
            self.addOneRow(root.right,val,depth-1)
        return root