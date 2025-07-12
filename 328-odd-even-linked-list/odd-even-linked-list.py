# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        p1 = head
        temphead = p1.next
        storehead = temphead
        while temphead and temphead.next:
            p1.next = temphead.next
            p1 = p1.next
            temphead.next = p1.next
            temphead = temphead.next
        p1.next = storehead
        return head
        

        