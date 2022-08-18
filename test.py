
# import imp
# from myfile import make_dir_if_not_exists

# import LeetCode
# from LeetCode import LeetCodeUtil
# LeetCodeUtil.printLstMarked([1],[0])

# make_dir_if_not_exists(r"D:\test")
# OSError: [WinError 123] 文件名、目录名或卷标语法不正确。: 'D:\test'

print(0.7*1.2*20)

# python 10进制  转化 2进制

print(bin(240))
# 0b11110000

print(bin(240)[2:])

# https://www.php.cn/python-tutorials-421751.html

# int('0b11110000', 2)
val=int('1111', 2)
print(val)

print(bin(192))
# 0b11000000

# 9*4^5
# res=9*pow(4,5)/2598960
# 0.0035460337981346383
# res=8*pow(4,5)/2598960
# # 0.0031520300427863453
# print(res)

# n! / ((n - m)! * m!) = 6

# res=60/(pow(10,4))

# print(res)

# 0.006

# res=pow(2,32)
# gailv=100*10000/res
# print(gailv)
# 0.00023283064365386963

# east=0.02/100*2/9
# west=0.03/100*7/9
# print(east/(west+east))
# 0.16

bananaPrice=11.8/3
print(bananaPrice)
# 3.9333333333333336
# def quickSort(list):
#     if len(list) <= 1:
#         return list
#     else:
#         pivot = list[0]
#         less = [i for i in list[1:] if i <= pivot]
#         greater = [i for i in list[1:] if i > pivot]
#         return quickSort(less) + [pivot] + quickSort(greater)