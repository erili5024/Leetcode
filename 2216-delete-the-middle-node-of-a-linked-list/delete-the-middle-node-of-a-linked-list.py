# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        counter = 0
        curr = head
        while curr:
            counter += 1
            curr = curr.next
        half = counter // 2
        curr = head
        i = 0 
        while i < half - 1:
            i += 1
            curr = curr.next
        curr.next = curr.next.next
        return head
        