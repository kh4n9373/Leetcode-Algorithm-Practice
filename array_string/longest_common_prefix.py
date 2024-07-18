class Solution:
    def longestCommonPrefix(self, strs) -> str:
        i = 0
        stack = []
        min_len = float('inf')
        for j in range(len(strs)):
            min_len = min(min_len,len(strs[j]))
        while i < min_len:
            stack.append(strs[0][i])
            for j in range(len(strs)):
                if strs[j][i] is stack[-1]:
                    continue
                else: 
                    stack.pop(-1)
                    return ''.join(stack)
            i += 1
        return ''.join(stack)


