
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

def make_one_dir(dir):
    dir_name=dir["name"]
    dir_apis=dir["item"]
    print("dir_name",dir_name)
    for i in dir_apis:
        one_func=make_one_api(i)
        print("one_func",one_func)
    # pass

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

def make_one_api(item_one_api):
    # item_one_api_name=item_one_api["name"]
    # print("item_one_api_name",item_one_api_name)
    # item_one_api=item_one_api["item"]
    print("item_one_api",item_one_api)
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


    controller_api_func=f"""
    

    @api_view([{method}])
    def {func_name}(request):
        
        url = "{raw}"

        payload='{payload}'
        headers = {header}

        response = requests.request("{method}", url, headers=headers, data=payload)

        print(response.text)
    """
    return controller_api_func

# 大括号
def get_key_brackets(key):
    return "{{"+key+"}}"

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
set_up_env_test()