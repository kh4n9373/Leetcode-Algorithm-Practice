# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: [ListNode]) -> int:
        stack,length,pointer = [],0,0
        res = 0
        cur = head
        left = head
        while cur:
            length += 1
            cur = cur.next
        while pointer <= length/2-1:
            stack.append(left.val)
            left = left.next
            pointer += 1
        while stack:
            l = stack.pop()
            r = left.val
            res = max(res,l+r)
            left = left.next
        return res
            
