
def printLstMarked(lst,markedIndexes):
    len_lst=len(lst)

    for i in range(len_lst):
        val=lst[i]
        if i in markedIndexes:
            print(f"({val})",end=" ") 
        else:
            print(f"{val}",end=" ") 
    print()