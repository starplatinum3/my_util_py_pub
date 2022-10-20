def func3(a, b, c):
    kwargs = locals()
    d = 'local_d'
    return kwargs
 
res = func3(1, 2, 3)
print(res)
# 结果
# {'c': 3, 'b': 2, 'a': 1}

# https://blog.csdn.net/weixin_33806509/article/details/92112864