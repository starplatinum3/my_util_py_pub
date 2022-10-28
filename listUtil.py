def list_same(list1, list2, list1_name, list2_name):
    not_in_list2 = []
    not_in_list1 = []
    for elm in list1:
        if elm not in list2:
            not_in_list2.append(elm)
    for elm in list2:
        if elm not in list1:
            not_in_list1.append(elm)

    # not_in_list1=[elm for elm in list2 and elm  not in list1]
    if len(not_in_list1)==0:
        print("可以凑出来")
    else:
        print("我们会得到:", list1, "。但是我们凑不出来:", not_in_list1, ",而且多凑出了:", not_in_list2)
        print("not in ", list1_name, "but in ", list2_name, ":", not_in_list1)
        print("not in ", list2_name, "but in ", list1_name, ":", not_in_list2)
    # print("not_in_list2 but in list1:",not_in_list2)


# list_same([1,2],[2,3])
import re


# def str_to_list(list_str="1 3 4 54"):
#     """
#     打印出列表里的数字然后粘贴到excel 然后转置
#     :param list_str:
#     :return:
#     """
#     result_list = re.split(r"[,\t 、]", list_str)
#     # result_list=[int(num.strip()) for num in result_list]
#     result = []
#     for num in result_list:
#         if num == "": continue
#         result.append(int(num.strip()))
#     # result_list.remove("")
#     return result

def str_to_list_re(list_str="1 3 4 54",split_by_re_str=r"[,\t 、，]"):
    # result_list=list_str.split(split_by)
    result_list = re.split(r"[,\t 、]", list_str)
    # result_list=[int(num.strip()) for num in result_list]
    result = []
    for num in result_list:
        if num == "": continue
        result.append(int(num.strip()))
    # result_list.remove("")
    return result


def str_to_list(list_str: str = "1 3 4 54", split_by: str = " ") -> list:
    """
    打印出列表里的数字然后粘贴到excel 然后转置
    :param list_str:
    :return:
    """
    result_list=list_str.split(split_by)
    # result_list = re.split(r"[,\t 、]", list_str)
    # result_list=[int(num.strip()) for num in result_list]
    result = []
    for num in result_list:
        if num == "": continue
        result.append(int(num.strip()))
    # result_list.remove("")
    return result


def str_rets_kind_to_list(list_str="1 3 4 54"):

    result_list = re.split("\n", list_str)
    # result_list=[int(num.strip()) for num in result_list]
    result = []
    for line in result_list:
        if line == "":
            continue
        result.append(line.strip())
    # result_list.remove("")
    return result


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
    """
    item.isspace()
    """
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

    