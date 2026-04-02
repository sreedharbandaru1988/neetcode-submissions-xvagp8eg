# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        prev_node = None       
        new_node = head
        dummy = ListNode()
        tail = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_list = slow.next
        slow.next = None
        while second_list:
            next_node = second_list.next
            second_list.next = prev_node
            prev_node = second_list
            second_list = next_node
        
        first, second = head, prev_node
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

