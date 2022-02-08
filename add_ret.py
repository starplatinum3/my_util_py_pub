
filename=r"G:\project\JSProject\经典小游戏吃豆人纯网页版游戏源代码下载_爱给网_aigei_com\38680\index.html"
with open(filename,"r") as f:
    data=f.read()

data=data.replace(";", ";\n")

out_filename=r"G:\project\JSProject\经典小游戏吃豆人纯网页版游戏源代码下载_爱给网_aigei_com\38680\index_ret.html"
# "r+" 不能直接写
# python 
with open(out_filename,"w") as f:
    f.write(data)