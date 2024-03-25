# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1, a, b, list2):
        cur = list1
        i = 0
        while i < a-1:
            cur = cur.next
            i += 1
        left = cur
        while i < b+1:
            cur = cur.next
            i += 1
        right = cur
        left.next = list2
        temp = list2
        while temp.next:
            temp = temp.next
        temp.next = right
        return list1