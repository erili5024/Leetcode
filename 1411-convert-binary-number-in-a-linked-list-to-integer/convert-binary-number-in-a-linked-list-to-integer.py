# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        temp = head
        counter = -1 
        sum = 0 
        while temp:
            counter += 1
            temp = temp.next
        temp = head
        while temp:
            sum = sum + temp.val * 2 ** counter
            counter = counter - 1
            temp = temp.next
        return sum

        