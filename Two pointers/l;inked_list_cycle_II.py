# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head:[ListNode]) -> [ListNode]:
        # I mean, this is a medium problem ???
        #O(n) space complexity
        
        seen = {}
        index = 0
        cur = head
        while cur and cur.next:
            if cur in seen:
                return cur
            seen[cur] = index
            cur = cur.next
            index += 1
        return None
    
