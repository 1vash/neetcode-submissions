# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
We change edges(lines), not swap values.

[  0->1->2->3]
[p->c->n]
# Rule: next -> prev [p <- n], curr+1


"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        # links are updated both for head & for curr as we use not deep copy!
        while curr:
            # as we break the next link by changing it, save it to tmp
            tmp_next = curr.next 
            
            curr.next = prev # move next pointer to the prev [p <- n]
            
            # move pointers to the right
            prev = curr # move prev pointer to the curr [p -> c]
            curr = tmp_next # move current pointer to the next

        return prev


