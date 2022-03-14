
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
def printLstMarked(lst,markedIndexes):
    len_lst=len(lst)

    for i in range(len_lst):
        val=lst[i]
        if i in markedIndexes:
            print(f"({val})",end=" ") 
        else:
            print(f"{val}",end=" ") 
    print()
