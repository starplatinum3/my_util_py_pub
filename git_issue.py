repoInfo = {}

from pyzing.mysql import msheet, mc, mo

address = {'host': 'localhost', 'user': 'root', 'passwd': '123456789', 'port': 3306, 'db':'test_db'}
mdb = msheet(address=address, sheet='test_sheet')

# js 翻译 python
def parseApi(crtUrl: str):
    # crtUrl.split()
    urlSplit = crtUrl.split('/')
    # //console.log(urlSplit)//list
    username = urlSplit[3]
    repopath = urlSplit[4]
    repoInfo.username = username
    repoInfo.repopath = repopath
    api = "https://api.github.com/repos/" + username + "/" + repopath

    # console.log("Get GitHub api URL:" + api)
    return api


import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
response = requests.get("http://www.baidu.com/s?", params=kw, headers=headers)


# python request
def reqIssData(apiUrl, pageNO):
    oriData = None
    kw = {
        "page": pageNO
    }
    # response = requests.get(apiUrl + "/issues?page=" + pageNO,params = kw, headers = headers)
    response = requests.get(apiUrl + "/issues", params=kw, headers=headers)
    issueInfo = response.text
    # response.text 转化json python
    pageIssuesNum = issueInfo.length
    if (pageNO == 1):
        repoInfo.newest = issueInfo[0].number
    if pageIssuesNum == None:
        print("Request failed.")
        return
    oriData = issueInfo
    return oriData

    # oriData = issueInfo;
    # $.ajax({
    #     url: apiUrl + "/issues?page=" + pageNO,
    #     type: "GET",
    #     async: false,
    # //dataType: "jsonp",
    # success: function (issueInfo) {
    #     console.log("issueInfo");
    # console.log(issueInfo);
    # var pageIssuesNum = issueInfo.length;
    # if (pageNO == 1) {
    #     repoInfo.newest = issueInfo[0].number;
    # }
    # if (pageIssuesNum == undefined) {
    # $("#status").text("Request failed.");
    # return;
    # }
    # oriData = issueInfo;
    # }
    # });
    # return oriData;

# api = "https://api.github.com/repos/" + username + "/" + repopath
