class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        left = dummy
        right = head
        
        # Step 1: Move right n steps ahead
        while n > 0:
            right = right.next
            n -= 1
        
        # Step 2: Move both until right reaches end
        while right:
            left = left.next
            right = right.next
        
        # Step 3: Remove the target node
        left.next = left.next.next
        
        return dummy.next  