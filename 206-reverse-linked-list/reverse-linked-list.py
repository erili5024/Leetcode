# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp = head
        first = head.next
        temp.next = None
        while first.next:
            nexts = first.next
            first.next = temp
            temp = first
            first = nexts
        first.next = temp
        return first
        
    