class Solution:
    def isHappy(self, n):
        visited = {n,}
        while True:
            n = sum(int(i)**2 for i in str(n))
            if n == 1:
                return True
            if n in visited:
                return False
            visited.add(n)
        return True