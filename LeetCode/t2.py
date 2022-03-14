# Definition for singly-linked list.
# from tkinter.messagebox import NO


# from .ListUtil import printLinkedList
# from .LeetCodeUtil import arrToLinkedList

from ListUtil import printLinkedList
from LeetCodeUtil import arrToLinkedList
# ModuleNotFoundError: No module named '__main__.ListUtil'; '__main__' is not a package

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# from tkinter.messagebox import NO



class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res =ListNode(-1)
        head=res
        # res=None
        node1=l1
        node2=l2
        carry=0
        node1End=False
        node2End=False
        while True:
            if node1==None:
                node1End=True
                break
            if node2==None:
                node2End=True
                break
            val=node1.val+node2.val+carry
            res.next=ListNode(val%10)
            # res=ListNode(val)
            # res.next
            res=res.next
            # 17/10== 1.. 7
            carry=val//10
            node1=node1.next
            node2=node2.next
        if node1End:
            while node2!=None:
                val=node2.val+carry
                res.next=ListNode(val%10)
                carry=val//10
                node2=node2.next
                res=res.next
        
        if node2End:
            while node1!=None:
                val=node1.val+carry
                res.next=ListNode(val%10)
                carry=val//10
                node1=node1.next
                res=res.next
        if carry>0:
            val=carry
            res.next=ListNode(val%10)
            res=res.next

        return head.next

Solution=Solution()
# l1 =arrToLinkedList([2,4,3])
# l2 =arrToLinkedList([5,6,4])

l1 =arrToLinkedList([0])
l2 =arrToLinkedList([0])

# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
# Solution=Solution()
res=Solution.addTwoNumbers(l1,l2)
# 0 
printLinkedList(res)

# ：l1 = [0], l2 = [0]
# 输出：[0]


