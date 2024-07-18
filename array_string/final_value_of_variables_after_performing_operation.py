class Solution:
    def finalValueAfterOperations(self, operations) -> int:
        x = 0
        for i in range(len(operations)):
            if '+' in operations[i]:
                x += 1
            elif '-' in operations[i]:
                x -= 1
        return x
        