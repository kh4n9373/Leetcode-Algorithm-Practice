# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head):
        '''
        count = 1
        cur = head
        while cur.next:
            count += 1
            cur = cur.next
        mid = count//2 
        while mid > 0:
            head = head.next
            mid -= 1
        return head
        '''
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
        
        