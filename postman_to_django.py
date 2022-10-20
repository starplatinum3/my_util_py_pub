
# python  读取 json 
import json


json_file=r"C:\Users\25004\AppData\Local\Postman\app-9.16.0\Salesforce Platform APIs.postman_collection.json"
env_json_file=r"C:\Users\25004\AppData\Local\Postman\app-9.16.0\Salesforce APIs Template Environment.postman_environment.json"
# 读取json文件内容,返回字典格式
with open(json_file,'r',encoding='utf8')as fp:
    json_data = json.load(fp)
    # print('这是文件中的json数据：',json_data)
    print('这是读取到文件数据的数据类型：', type(json_data))
with open(env_json_file,'r',encoding='utf8')as fp:
    env_json_data = json.load(fp)
   
# values[]
# 

env_values=env_json_data["values"]
print("env_values",env_values)
#  [{'key': 'url', 'value': 'https://test.salesforce.com', 'type': 'text', 'enabled': True}, {'key': 'version', 'value': '53.0', 'type': 'text', 'enabled': True}, 
item=json_data["item"]

# def make_func_name(path):
#     path=path[1:]
#     path=path.replace("/","_")
#     return path
def make_func_snake_name(path_part):
    return path_part.replace("{{","_").replace("}}","_").replace("-","_").replace(".","_")

def make_func_name(path):
    # path.join("_")
    # map python  转化 replace 
    # map(make_func_snake_name,path)
    path=list(map(make_func_snake_name,path))
    if "" in path:
        path.remove("")
    # print("path",path)
    # for i in path:
    #     if i=="/":
    #         i="_"
    # path=path[1:]
    # path=path.replace("/","_")
    # AttributeError: 'list' object has no attribute 'join'
    # python AttributeError: 'list' object has no attribute 'join'
    return "_".join(path)
    # return path.join("_")

def make_func_name_test():
    path="/services/data/v49.0/sobjects/Account"
    # path=[ ]
    path=path.split("/")
    # path=path[1:]
    # path=path.replace("/","_")
    res=make_func_name(path)
    print("res")
    print(res)
from urllib.parse import urlencode

# python  转化 url encode 
def make_query_key_val(query_pair):
    key=query_pair["key"]
    value=query_pair["value"]
    return key+"="+value
    # pass

def query_to_payload(query):
    for i  in query:
        key=i["key"]
        value=i["value"]
        print(key,value)
    pass

def query_to_map(query):
    query_map={}
    for i in query:
        key=i["key"]
        value=i["value"]
        query_map[key]=value
    return query_map

def to_file_path_name(filename:str):
    filename=filename.strip()
    filename = filename.replace(" ", "_")
    # https://www.cnblogs.com/jjliu/p/11514226.html
    filename = filename.replace(":", "")
    return filename

def to_python_underscore_name(filename:str):
    filename=filename.strip()
    filename = filename.replace(" ", "_")
    # https://www.cnblogs.com/jjliu/p/11514226.html
    filename = filename.replace(":", "").replace("(", "").replace(")", "")
    
    return filename.lower()

import time_util
code_gen_dir=r"D:\codeGenPostmanToDjango"
# to_python_snake 
now_time_str=time_util.get_now_time_str()
# os.path
import os 
do_write_file=False
# do_write_file=True
this_gen_dir=os.path.join(code_gen_dir,now_time_str)
if do_write_file:
    os.makedirs(this_gen_dir)
print("this_gen_dir",this_gen_dir)

def check_and_write_file(col_dir_name,data):
    if do_write_file:
        with open(col_dir_name,'w',encoding='utf8') as fp:
            fp.write(data)
    # if do_write_file:
    #     os.makedirs(col_dir_name)

def check_and_make_dirs(col_dir_name):
    if do_write_file:
        os.makedirs(col_dir_name)

def get_recursively(search_dict, field):
    """
    https://stackoverflow.com/questions/14962485/finding-a-key-recursively-in-a-dictionary
    Takes a dict with nested lists and dicts,
    and searches all dicts for a key of the field
    provided.
    获取包含嵌套列表和dict的dict，
并搜索所有dict以查找字段的键
假如
    """
    fields_found = []

    # for key, value in search_dict.iteritems():
    for key, value in search_dict.items():

        if key == field:
            fields_found.append(value)

        elif isinstance(value, dict):
            results = get_recursively(value, field)
            for result in results:
                fields_found.append(result)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    more_results = get_recursively(item, field)
                    for another_result in more_results:
                        fields_found.append(another_result)

    return fields_found

    # https://stackoverflow.com/questions/14962485/finding-a-key-recursively-in-a-dictionary

def dfs(dirs,dir_name):
    funcs=""
    # req_name=dirs["name"]
    # print("req_name",req_name)
    # controller_name=to_python_underscore_name(req_name)
    # # col_dir_name=os.path.join(this_gen_dir,dir_name)
    # controller_path=os.path.join(this_gen_dir,f"{controller_name}_controller.py")
    # # print("col_dir_name",col_dir_name)
    # print("controller_path",controller_path)
    # # if do_write_file:
    # #     os.makedirs(col_dir_name)
    # # check_and_write_file(controller_path)
    
    # print("controller_name",controller_name)
    controller_name=to_python_underscore_name(dir_name)
    # controller_name=to_python_underscore_name(req_name)
    # # col_dir_name=os.path.join(this_gen_dir,dir_name)
    controller_path=os.path.join(this_gen_dir,f"{controller_name}_controller.py")
    # # print("col_dir_name",col_dir_name)
    print("controller_path",controller_path)
    # # if do_write_file:
    # #     os.makedirs(col_dir_name)
    # # check_and_write_file(controller_path)
    
    print("controller_name",controller_name)
    for req in dirs:
        # dir_apis=dir["item"]
        # dir_name=dir["name"]
        # req_name=req["name"]
        # print("req_name",req_name)
        # dir_name=
        
        if "request" in req:
            # print(i)
            
            request= req["request"]
            # print(i["request"])
            one_func,func_name=make_one_api(req)
            funcs+=one_func+"\n\n"
            # pass
            request=req["request"]
            url=request["url"]
            method=request['method']
            raw=url['raw']
            # print
            url_path=f"path('{raw}',{controller_name}_controller.{func_name},name='{func_name}'),"
            print(one_func)
        if "item" in req:
            # req["name"]
            dfs(req["item"],req["name"])


def make_one_dir(dir):
    try:
        dir_name=dir["name"]
    except Exception  as e:
        print("dir",dir)
        print(e)
    if "item" not in dir:
        print("没有更加下面的目录了 ")
        print("dir ",dir)
        one_func,func_name=make_one_api(dir)
        # print("one_func",one_func)
        # funcs+=one_func+"\n\n"
    # pass
        request=dir["request"]
        url=request["url"]
        method=request['method']
        raw=url['raw']
        # print
        print("dir_name",dir_name)
        controller_name=to_python_underscore_name(dir_name)
        url_path=f"path('{raw}',{controller_name}_controller.{func_name},name='{func_name}'),"
        return 

    dir_apis=dir["item"]
    print("dir_name",dir_name)
    controller_name=to_python_underscore_name(dir_name)
    # col_dir_name=os.path.join(this_gen_dir,dir_name)
    controller_path=os.path.join(this_gen_dir,f"{controller_name}_controller.py")
    # print("col_dir_name",col_dir_name)
    print("controller_path",controller_path)
    # if do_write_file:
    #     os.makedirs(col_dir_name)
    # check_and_write_file(controller_path)
    
    print("controller_name",controller_name)
    # {controller_name}_controller.py
    # os.path.join(this_gen_dir,dir_name)
    # check_and_write_file(os.path.join(col_dir_name,f"{controller_name}_controller.py"))
    funcs=""
    for i in dir_apis:
        # ValueError: not enough values to unpack (expected 2, got 0)
        one_func,func_name=make_one_api(i)
        # print("one_func",one_func)
        funcs+=one_func+"\n\n"
    # pass
        request=i["request"]
        url=request["url"]
        method=request['method']
        raw=url['raw']
        # print
        url_path=f"path('{raw}',{controller_name}_controller.{func_name},name='{func_name}'),"
        # print(url_path)
    # with open(controller_path,'w',encoding='utf8') as fp:
    #     fp.write(funcs)
    check_and_write_file(controller_path,funcs)

def make_paylaod(url):
    if "query" not in url:
        return ""
    query=url['query']
    query_map= query_to_map(query)
    payload=urlencode(query_map)
    return payload
    pass

def head_to_python_req_headers(head):
    headers_map={}
    # head['key']
    for i in head:
        key=i['key']
        value=i['value']
        headers_map[key]=value
    return headers_map
    pass

import re
def make_params(all_braks):
    res=""
    for i in all_braks:
        res+=" , "+i
    return res

def make_one_api(item_one_api):
    # if "item" in item_one_api:
    #     # make_one_api()
    #     # dir
    # #     dir_name=dir["name"]
    # # dir_apis=dir["item"]
    #     # make_one_dir(item_one_api["item"])
    #     item=item_one_api["item"]
    #     for one_dir in item:
    #         make_one_dir(one_dir)

    # item_one_api_name=item_one_api["name"]
    # print("item_one_api_name",item_one_api_name)
    # item_one_api=item_one_api["item"return ""]
    # print("item_one_api",item_one_api)
    if "request" not in item_one_api:
        print("item_one_api",item_one_api)
        return ""
    request=item_one_api["request"]
    url=request["url"]
    method=request['method']
    raw=url['raw']
    # raw_mode_data=request["body"]["raw"]
    # item_one_api["request"]["url"]["raw"]
    path=url["path"]
    func_name=make_func_name(path)
    header=request['header']
    header=head_to_python_req_headers(header)
    # headers = [{'key': 'Content-Type', 'name': 'Content-Type', 'value': 'text/xml; charset=UTF-8', 'type': 'text'}, {'key': 'SOAPAction', 'value': 'login', 'type': 'text'}, {'key': 'Accept', 'value': 'text/xml', 'type': 'text'}]
    # query=url['query']
    # query_map= query_to_map(query)
    # payload=urlencode(query_map)
    payload=make_paylaod(url)
    # raw.replace("{{instance_url}}","instance_url")


    # url = "{raw}"
    
    # mark_str="{raw}"
    # url=set_up_env(env_values,mark_str)
    all_res=re.findall("{{(.*?)}}", raw)                                                                             
    # all_res                                                                                                             
    # ['_endpoint', 'version', '_jobId'] 
    # print("all_res",all_res)
    # params=",".join(all_res)
    params=make_params(all_res)
    # al 
    # ",".join(all_res)
    # python 函数参数 拿到
    # kwargs = locals()
    # d = 'local_d'
    # return kwargs

    controller_api_func=f"""
    
@api_view([{method}])
def {func_name}(request {params}):
    kwargs = locals()
    url = "{raw}"
    # url=set_up_env(kwargs,url)
    url=set_up_env_by_map(kwargs,url)
    payload='{payload}'
    headers = {header}

    response = requests.request("{method}", url, headers=headers, data=payload)

    print(response.text)
    """
    return controller_api_func,func_name

# 大括号
def get_key_brackets(key):
    return "{{"+key+"}}"

def set_up_env_by_map(env_values,mark_str):
    # for i in env_values:
    for key,value in env_values.items():
        # key=i["key"]
        # value=i["value"]
        key_brackets=get_key_brackets(key)
        # mark_str=mark_str.replace(key_brackets,key)
        mark_str=mark_str.replace(key_brackets,value)
  
    return mark_str

# final_str {{_endpoint}}/services/data/v53.0/async-queries/{{_jobId}}
def set_up_env(env_values,mark_str):
    for i in env_values:
        key=i["key"]
        value=i["value"]
        key_brackets=get_key_brackets(key)
        # mark_str=mark_str.replace(key_brackets,key)
        mark_str=mark_str.replace(key_brackets,value)
        # print(key,value)
    # env_name=env["name"]
    # env_value=env["value"]
    # env_str=f"""
    # {env_name}="{env_value}"
    # """
    return mark_str


# for item_one_api in item:
#     item_one_api["item"]

#     request=item_one_api["request"]
#     url=request["url"]
#     item_one_api["request"]["url"]["raw"]


# item0=item[0]

# # print(item0["name"])

# item0_request=item0["request"]

# item0_request_url=item0_request["url"]
# item0_request_url_raw=item0_request_url["raw"]
# item0_request_method=item0_request["method"]

# django rest controller 
# https://www.django-rest-framework.org/api-guide/serializers/

# from django.shortcuts import render

# from django.http.response import JsonResponse
# from rest_framework.parsers import JSONParser 
# from rest_framework import status

# from tutorials.models import Tutorial
# from tutorials.serializers import TutorialSerializer
# from rest_framework.decorators import api_view

# item0_request_method="1"
# controller_api_func=f"""

# @api_view([{item0_request_method}])
# def tutorial_list(request):
#     if request.method == 'GET':
#         tutorials = Tutorial.objects.all()

#         title = request.query_params.get('title', None)
#         if title is not None:
#             tutorials = tutorials.filter(title__icontains=title)

#         tutorials_serializer = TutorialSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)
#         # 'safe=False' for objects serialization

#     elif request.method == 'POST':
#         tutorial_data = JSONParser().parse(request)
#         tutorial_serializer = TutorialSerializer(data=tutorial_data)
#         if tutorial_serializer.is_valid():
#             tutorial_serializer.save()
#             return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
#         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         count = Tutorial.objects.all().delete()
# """

# make_func_name_test()

# make_one_api(item[0])

# make_one_dir(item[0])
def main_run():
    for i in item:
        make_one_dir(i)

# @api_view([DELETE])
#     def services_data_v_version__async_queries___jobId_(request):

#         url = "{{_endpoint}}/services/data/v{{version}}/async-queries/{{_jobId}}"

#         payload=''
#         headers = [{'key': 'Content-Type', 'value': 'application/json'}]

#         response = requests.request("DELETE", url, headers=headers, data=payload)

#         print(response.text)

def set_up_env_test():
    mark_str= "{{_endpoint}}/services/data/v{{version}}/async-queries/{{_jobId}}"
    print("env_values",env_values)
    final_str=set_up_env(env_values,mark_str)
    
    print("final_str",final_str)
# set_up_env_test()

# main_run()


# 请问python正则如何匹配两个大括号，比如{{_endpoint}}
import re
string  = "{{_endpoint}}/services/data/v{{version}}/async-queries/{{_jobId}}"
# string = 'shain(love)fufu)'
# p1 = re.compile(r'[(](.*?)[)]', re.S) #最小匹配
brackets = re.compile(r'[{{](.*?)[}}]', re.S) #最小匹配
# all_res ['{_endpoint', '{version', '{_jobId']
# 哦 这个最小匹配 有了 然后前面的 { 删掉就行吗 

# brackets = re.compile(r'[{{](.*)[}}]', re.S) #贪婪匹配
# all_res ['{_endpoint}}/services/data/v{{version}}/async-queries/{{_jobId}']


# brackets = re.compile(r'{{(.*)}}', re.S) #贪婪匹配
# all_res ['_endpoint}}/services/data/v{{version}}/async-queries/{{_jobId']

# brackets = re.compile(r'{{(.*)}}', re.S) #贪婪匹配
# p2 = re.compile(r'[(](.*)[)]', re.S)  #贪婪匹配
# all_res=re.findall(brackets, string)
# print(re.findall(brackets, string))
# print(re.findall(p2, string))
# print("all_res",all_res)
# all_res ['{_endpoint', '{version', '{_jobId']

all_res=re.findall("{{(.*?)}}", string)                                                                             
# all_res                                                                                                             
# ['_endpoint', 'version', '_jobId'] 
# print("all_res",all_res)
# all_res ['_endpoint', 'version', '_jobId']

# params=",".join(all_res)
# print("params",params)
# params _endpoint,version,_jobId

# res=get_recursively(json_data,"item")
# print("res",res)
# print("res",res[4])
# print("res",res[0])
dfs(item,"root_dir")