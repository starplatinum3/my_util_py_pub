

# from tkinter.messagebox import NO


def printLinkedList(LinkedList):
    node =LinkedList
    while node!=None:
        print(node.val,end=" ")
        node=node.next
    print()



# listUtil.py
def remove_all(lst: list, what):
    ret_lst = []
    for item in lst:
        # https://www.cnblogs.com/jiyongjia/p/9539024.html
        if what == item: continue
        # print("what",what)
        # print("item",item)
        ret_lst.append(item)
        # ret_lst.append(item)
        # pass
    return ret_lst

# python 判断字符串是 空，空格
# https://www.itranslater.com/qa/details/2127291587607659520
def remove_none(lst: list):
    ret_lst = []
    for item in lst:
        # https://www.cnblogs.com/jiyongjia/p/9539024.html
        # if item is None:
        #     continue
        # if item =="":
        #     continue
        if not item or item.isspace():
            continue

        # if what == item: continue
        # print("what",what)
        # print("item",item)
        ret_lst.append(item)
        # ret_lst.append(item)
        # pass
    return ret_lst

    