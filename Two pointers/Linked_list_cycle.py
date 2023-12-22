# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head:[ListNode]) -> bool:
        '''
        #O(n) space complexity
        seen = {}
        index = 0
        cur = head
        while cur and cur.next:
            if cur in seen:
                return True
            seen[cur] = index
            cur = cur.next
            index += 1
        return False
        '''
        tortoise , hare = head, head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return True
        return False