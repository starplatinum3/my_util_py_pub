

# from tkinter.messagebox import NO


def printLinkedList(LinkedList):
    node =LinkedList
    while node!=None:
        print(node.val,end=" ")
        node=node.next
    print()

