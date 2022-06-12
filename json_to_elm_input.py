

# from asyncore import file_dispatcher

import json

file_path=r"D:\newfit\newfit-vue\user1.json"
with open(file_path,'r',encoding='utf-8') as load_f:
    load_dict = json.load(load_f)
# D:\newfit\newfit-vue\user.json
inputs_str=""
# query_str="query: {"
query_str=""
# query_wrapper=
java_dto=""
for field_name in load_dict:
    # print(field_name)
    # field_val=load_dict[field_name]
    # print(load_dict[field_name])
    query_str+=f'     {field_name}: null,\n'
    java_dto+=f'private String {field_name};\n'
    inputs_str+=f'<el-input v-model="query.{field_name}" placeholder="用户名" class="handle-input mr10"></el-input>\n'
# <el-input v-model="query.userName" placeholder="用户名" class="handle-input mr10"></el-input>
query_wrapper="query: {\n"+query_str+ "}"
# query_str+=
print("inputs_str")
print(inputs_str)
print("===========")
print("query_wrapper")
print(query_wrapper)
print("===========")
print("java_dto")
print(java_dto)

# D:\proj\python\my_util_py_pub>python "d:\proj\python\my_util_py_pub\json_to_elm_input.py"
# Traceback (most recent call last):
#   File "d:\proj\python\my_util_py_pub\json_to_elm_input.py", line 3, in <module>
#     from asyncore import file_dispatcher
# ImportError: cannot import name 'file_dispatcher' from 'asyncore' (D:\software\anaconda\lib\asyncore.py)
