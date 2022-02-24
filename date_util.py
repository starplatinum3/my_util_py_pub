


# def parse_date(date_str):
# #     retrun time.strftime("%Y.%m.%d",date_str)
#     date_str=str(date_str)
#     if date_str=="nan":
#         return ""
#     try:
#         date=time.strptime(date_str,"%Y.%m.%d")
#         date_str_ok=time.strftime("%Y/%m/%d",date)
#         return date_str_ok
#     except ValueError:
#         return date_str
#     return time.strptime(date_str,"%Y.%m.%d")

# https://www.cnpython.com/qa/118360
import datetime

def split_dot(date_str:str):
    sps=date_str.split(".")
    day=sps[2]
    # print(sps)
    if int(day)>31:
        return
    print(date_str)

class DateUtil:
    # def __init__(self):
    dotYmd="%Y.%m.%d"
    
    # [DateUtil.dotYmd 写这个 不行
    DATE_FORMATS = [dotYmd,'%Y年%m月%d日','%m/%d/%Y %I:%M:%S %p', 
    '%Y/%m/%d %H:%M:%S', '%d/%m/%Y %H:%M', '%m/%d/%Y', '%Y/%m/%d',
    "%Y%m%d","%Y、%m","%Y.%m","%Y","%Y.%m.","%Y.%m.%d."]

    @staticmethod
    def parse_date_of_fmt_str(date_str,fmt_str):
        try:
            return datetime.datetime.strptime(date_str,fmt_str)
        except:
            return None

    @staticmethod
    def rm_not_num_or_dot(string):
        out_str=""
        for ch in string:
            # if ch.isnum():
            # if ch.isnumeric():
            if ch.isdigit():
                # isnumeric()
                out_str+=ch
            elif ch =='.':
                out_str+=ch
        return out_str
    
    @staticmethod
    def parse_date_of_many_fmt(date_str):
        fmt_str_lst=DateUtil. DATE_FORMATS
        for fmt in fmt_str_lst:
            date=DateUtil.parse_date_of_fmt_str(date_str,fmt)
            if date!=None:
                return date
        return None

    @staticmethod
    def parse_date(date_str):

        date_str=str(date_str)
        if date_str=="43943":
            print(43943)
        if date_str is None:
            return None
        if date_str=="":
            return None
        moved_str=date_str
        # moved_str=move_not_date_form(date_str)
        if(moved_str.endswith("年")):
            date=datetime.datetime(int(moved_str[:-2]),1,1)
            return date
        #  isnumeric 中文的四 他也是当作可以的。。
        # if(moved_str.isnumeric()):
            # isdigit ()
        if   moved_str.isdigit():
            date=DateUtil. parse_date_of_fmt_str(date_str,"%Y%m%d")
            if date !=None:
                return date
            # if date==None:
            date=datetime.datetime(int(moved_str),1,1)
            return date
    #     https://www.runoob.com/python/att-string-isnumeric.html
    #     isnum str
        # fmt_str_lst=[DateUtil.dotYmd,'%Y年%m月%d日']
        # fmt_str_lst=DateUtil. DATE_FORMATS
        
        try:
            date= pd.to_datetime(moved_str)
    #         datetime.datetime.strptime(moved_str,'%Y年%m月%d日')
        except:
            date=DateUtil.parse_date_of_many_fmt(moved_str)
            if date!=None:
                return date
            # for fmt in fmt_str_lst:
            #     date=DateUtil.parse_date_of_fmt_str(moved_str,fmt)
            #     if date!=None:
            #         return date
            # print(moved_str)
            moved_str=DateUtil.rm_not_num_or_dot(moved_str)
            date=DateUtil.parse_date_of_many_fmt(moved_str)
            if date!=None:
                return date
            # print(moved_str)
            # moved_str.split(".")
            try:
                split_dot(moved_str)
            except:
                if moved_str!="":
                    print(moved_str)
            return None
            # while True:
            #     date=parse_date_of_fmt_str(moved_str,)
            # try:
            #     date=datetime.datetime.strptime(moved_str,'%Y年%m月%d日')
            # except:
            #     try:
            #         date=datetime.datetime.strptime(moved_str,'%Y年')
            #     except  AttributeError:
            #         print(moved_str)

# data['首播日期'].apply(lambda x:parse_date(x))

# data['首播日期']=data['首播日期'].apply(lambda x:datetime.datetime.strptime(move_not_date_form(x),'%Y年%m月%d日'))


# str1="2017/4/1"
# date1= pd.to_datetime(str1)
# date1


import re

# https://www.cnblogs.com/guxingy/p/12890053.html
# UnboundLocalError: local variable 'strdate' referenced before assignment

def move_not_date_form(string):
#     str1='访客-2020-03-22 235119.xlsx'
    if not string.find("("):
        return string
    m = re.search("(\d{4}年\d{1,2}月\d{1,2}日)", string)
#     print(type(m))
    try:
        strdate = m.group(1)
    except AttributeError as e:
        print(string)
        print(e)
        raise

#     print(strdate)
    return strdate

# str1="2001年7月28日 (Fantasia International Film Festiv...	"
# print(move_not_date_form(str1))


# data[data["首播日期"]>=y_2000]

# pd 两个条件
# https://blog.csdn.net/GeekLeee/article/details/75268762
# ani_00_to_10=data[(2000<data["首播日期"])&(data["首播日期"]<=2010)]

# G:\file\学校\python数据分析\大作业代码\bangumi.ipynb

# print(parse_date("1995.12.20"))

# print(parse_date("2020年4月22日"))


# print(DateUtil. parse_date("1995.12.20"))

# print(DateUtil.parse_date("2020年4月22日"))

# str1=DateUtil.rm_not_num_or_dot("2011、12")
# print(str1)