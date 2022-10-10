# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_pointer, current_pointer = None, head

        # Loop until the end of the list
        while current_pointer:
            holding_pointer = current_pointer.next
            current_pointer.next = previous_pointer

            # Update pointers to point next items
            previous_pointer = current_pointer
            current_pointer = holding_pointer

        # previous_pointer will point to the last item of the list
        # which would be the head of the reversed list
        return previous_pointer
        