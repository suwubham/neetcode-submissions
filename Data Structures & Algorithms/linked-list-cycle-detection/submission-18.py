# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # seen = set()
        # current_node = head
        # while current_node:
        #     if current_node in seen:
        #         return True
        #     seen.add(current_node)
        #     current_node = current_node.next
        
        # return False

        # Turtle and Hare Approach
        slow = head
        fast = head
        while slow and fast:            
            slow = slow.next
            fast = fast.next
            if not fast:
                return False
            fast = fast.next

            if fast == slow:
                return True
        
        return False