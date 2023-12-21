# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        s1, s2 = '', ''
        while l1:
            s1 += str(l1.val)
            l1 = l1.next
        while l2:
            s2 += str(l2.val)
            l2 = l2.next
        s = str(int(s1[::-1]) + int(s2[::-1]))[::-1]
        dummy = ListNode()
        cur = dummy
        for i in s:
            cur.next = ListNode(int(i))
            cur = cur.next
        return dummy.next

