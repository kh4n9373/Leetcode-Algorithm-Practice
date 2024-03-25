class Solution:
    def getRow(self, rowIndex: int):
        
        def cal(arr):
            return [arr[i] + arr[i+1] for i in range(len(arr)-1)]

        def dfs(r):
            if r == 0:
                return [1]
            if r == 1:
                return [1,1]
            return [1] + cal(dfs(r-1)) + [1]
        return dfs(rowIndex)
