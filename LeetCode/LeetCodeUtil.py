
# from .ListNode import ListNode
from ListNode import ListNode

# ListNode

def arrToLinkedList(arr):
    dummyHead=ListNode(-1)
    node=dummyHead
    # node=
    for i in arr:
        node.next=ListNode(i)
        node=node.next
    return dummyHead.next
