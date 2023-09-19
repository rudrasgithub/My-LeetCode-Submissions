# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return 
        curr=ListNode()
        curr.next=head
        ref=curr
        while ref.next:
            if ref.next.val==val:
                ref.next=ref.next.next
            else:
                ref=ref.next
        return curr.next
