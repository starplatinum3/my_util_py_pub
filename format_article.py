
# read_path="C:\\Users\\Administrator\\Desktop\\"
read_path=r"D:\proj\python\my_util_py_pub\aritcle.txt"
print("从这里读",read_path)
with open(read_path, 'r') as f:
    article= f.read()

# for i i 
lines=article.split("\n")
data=""
for line in lines:
    data+=" "+line
# print(data)

out_path="data_formated.txt"
print("写入",out_path)
with open(out_path,"w") as f:
    f.write(data)