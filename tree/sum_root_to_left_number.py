class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        sum = 0
        def dfs(root, res=''):
            nonlocal sum
            res += str(root.val)
            if not root.left and not root.right:
                sum += int(res)
                return res
            temp = res
            if root.left:
                res += dfs(root.left, res)
            res = temp
            if root.right:
                res += dfs(root.right, res)
            return res
        dfs(root)
        return sum
        