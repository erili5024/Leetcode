# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head and not head.next:
            return 0 
        temp = head
        number = []
        max = 0 
        sum = 0 
        while temp:
            number.append(temp.val)
            temp = temp.next
        p1 = 0 
        p2 = len(number) - 1
        while p1 < p2:
            sum = number[p1] + number[p2]
            if sum > max:
                max = sum
            p1 += 1
            p2 -= 1 
        return max


        