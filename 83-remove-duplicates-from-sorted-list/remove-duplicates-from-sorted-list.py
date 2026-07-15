# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vis=set()
        while head:
            vis.add(head.val)
            head=head.next
        vis=sorted(vis)
        node=ListNode()
        curr=node
        for i in vis:
            curr.next=ListNode(i)
            curr=curr.next
        return node.next
