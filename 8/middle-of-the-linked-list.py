# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        fast = head
        slow = head

        move = False

        while(fast):
            fast = fast.next
            slow = slow.next if move else slow
            move = not move

        return slow.next
