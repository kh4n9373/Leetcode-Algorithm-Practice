# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        dic = {}
        for i,a in enumerate('abcdefghijklmnopqrstuvwxyz'):
            dic[i] = a
        stack = []
        def dfs(root,s=''):
            nonlocal stack
            if not root:
                return 
            s += dic[root.val]
            if not root.left and not root.right:
                stack.append(s[::-1])
                return 
            dfs(root.left,s)
            dfs(root.right,s)
            return
        dfs(root)
        return min(stack)


        