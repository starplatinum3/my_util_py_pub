# -*- coding: utf-8 -*-
# from appdirs import unicode
# from numpy import unicode
import re

# 前面加 0 ， 1变成 0001 ，22 -> 0022
def make_str_some_what(str: str, wholeLen: int, what: str):
    lenStr = len(str)
    toAdd = wholeLen - lenStr
    prefix = ""
    for i in range(toAdd):
        prefix += what

    return prefix + str

# wholeLen 总长度，4 -> 0001
def make_str_some_0(str: str, wholeLen: int):
    return make_str_some_what(str, wholeLen, '0')


def make_str_4_0(str: str):
    return make_str_some_0(str, 4)


# https://blog.csdn.net/mouday/article/details/81512870
def contains_chinese(check_str):
    """
    判断字符串中是否包含中文
    :param check_str: {str} 需要检测的字符串
    :return: {bool} 包含返回True， 不包含返回False
    """
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def is_chinese(string):
    """
    检查整个字符串是否为中文
    Args:
        string (str): 需要检查的字符串,包含空格也是False
    Return
        bool
    """
    for chart in string:
        if chart < u'\u4e00' or chart > u'\u9fff':
            return False

    return True



def format_post_data(headers_str):
    pattern = '^(.*?):(.*)$'
    for line in headers_str.splitlines():
        print(re.sub(pattern, '\'\\1\':\'\\2\',', line))


# https://blog.csdn.net/i_chaoren/article/details/77922939
def test():
    str = "114"
    # "{0:4}".format(str)
    # print(str)
    str = make_str_4_0(str)
    print(str)


def test_isalpha():
    str = "a.不正常的"
    print(str.isalpha())
    print(str[-1].isalpha())
    print(str[-1])
    print(isalpha(str), str)
    print(isalpha(str[-1]), str[-1])


def isalpha(char):
    return "a" <= char <= "z" or "A" <= char <= "Z"


# https://blog.csdn.net/xiaoxiaoley/article/details/78624953
def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """
    dict0 = {}
    for i in range(26):
        dict0[chr(ord('A') + i)] = i + 1

    output = 0
    for i in range(len(s)):
        output = output * 26 + dict0[s[i]]

    return output


def test_titleToNumber():
    # print(titleToNumber('AA'))
    # print(titleToNumber('X'))
    print(titleToNumber('W'))
    print(titleToNumber('Y'))
    print(titleToNumber('AB'))


class Test:
    def test_make_str_some_0(self):
        for i in range(4, 34):
            print(make_str_some_0(str(i), 2))


def sub_strs_start_end_all(str, start, end):
    # https://zhidao.baidu.com/question/2057789258998428427.html
    things = list()
    # https://www.cnblogs.com/xingchuxin/p/10427391.html
    while True:
        start_pos = str.find(start)
        if start_pos == -1:
            break

        end_pos = str.find(end)
        if end_pos == -1:
            break
        while True:
            # https://blog.csdn.net/weixin_33739523/article/details/93816000
            startAnotherPos = str.find(start, start_pos + 1)
            # 如果有不符合的字符串，比如说https:3,https:4.jar,3后面没有.jar，就要把3的这个去掉
            # 如果https后面还有个https，但是中间没有.jar，说明前面的https是不正确的格式，要舍去
            if startAnotherPos == -1:
                break
            if startAnotherPos < end_pos:
                start_pos = startAnotherPos
            if start_pos > end_pos:
                end_another_pos = str.find(end, end_pos + 1)
                end_pos = end_another_pos
            else:
                break
        sub_str = str[start_pos:end_pos] + end

        things.append(sub_str)

        str = str[end_pos + len(end):]
    things_final = list()
    # 这边不知道为什么会有不是以start开头的也被过滤进来了，想搞清楚太麻烦，还是再过滤一次好了
    for thing in things:
        if thing.startswith(start):
            things_final.append(thing)
    return things_final


def get_num(str="26-35: IOJBC KHDAF"):
    #     26-35: IOJBC KHDAF
    # 36-45: FCMEG NHBJD
    # 46-55: DACAB DCADB

    num_and_letters = str.split(":")
    num_str = num_and_letters[0].split("-")
    start_num = int(num_str[0])
    end_num = int(num_str[1])
    letters = num_and_letters[1]
    # letters.replace(" ","")
    # print("letters:",letters)
    # remove(letters," ")
    letters = letters.replace(" ", "")
    # print("letters:",letters)
    # print("encode:",letters.encode())
    # print(unicode("人生苦短", "utf-8"))
    j = 0
    for i in range(start_num, end_num + 1):
        print(i, ":", letters[j], end=",  ")
        j += 1


def remove(str, to_remove):
    ret = ""
    to_remove_len = len(to_remove)
    str_len = len(str)
    i = 0
    while True:
        sub_str = str[i:i + to_remove_len]
        # print("sub_str:",sub_str)
        if sub_str == to_remove:
            # print("sub_str:",sub_str)
            i += 1
            continue
        else:
            ret += sub_str
            i += 1
            if i > str_len - to_remove_len:
                break

    return ret


def get_nums():
    strs = ["26-35: IOJBC KHDAF",
            "36-45: FCMEG NHBJD",
            "46-55: DACAB DCADB"]
    for str in strs:
        get_num(str)


def str_to_unicode(str):
    unicodes = ''
    for chr in str:
        unicodes += r'\u{}'.format(ord(chr))
    return unicodes


def batch_sql_insert_str():
    str = ""
    for i in range(13, 47 + 1):
        str += f"({i},2),"
    print(str)


def one_slash_to_two(str):
    return str.replace("\\", "\\\\")


def remove_dont_want_sql_elm(string):
    pattern = "[m2\.`.+` as .+]"
    # https://blog.csdn.net/qq_26442553/article/details/82754722
    ret = re.match(pattern, string).group()
    re_match = re.match(pattern, string)
    print(1)
    print(ret)
    print(re_match)


def test_re():
    str1 = "abcABC*?//"
    str2 = "3afasdlfadsf"
    ret2 = re.match("[a-z]", str1).group()  # a
    ret3 = re.match("[123456]", str2).group()  # 3,[1-6]等价[123456]
    print("ret2:", ret2)
    print("ret3:", ret3)
    string = ""
    ret4 = re.match("[`.`]", "`1`").group()
    print("ret4:", ret4)


def test_unicode():
    str1 = "我爱派森"

    print(str1.decode('UTF-8'))


def r_del_str(old_str, dont_want):
    if dont_want == "":
        return old_str
    old_str_len = len(old_str)
    dont_want_len = len(dont_want)
    i_old = old_str_len - 1
    i_dont = dont_want_len - 1

    i_res = old_str_len
    i_now = old_str_len
    while 1:
        if not old_str[i_old] == dont_want[i_dont]:
            return old_str[:i_res]
        i_now -= 1
        if i_res - i_now == dont_want_len:
            i_res -= dont_want_len
        if i_dont == 0 or i_old == 0:
            return old_str[:i_res]

        i_old -= 1
        i_dont -= 1


def front_del_str(old_str, dont_want):
    if dont_want == "":
        return old_str
    old_str_len = len(old_str)
    dont_want_len = len(dont_want)
    min_len = min(old_str_len, dont_want_len)
    i_old = 0
    i_dont = 0

    i_res = 0
    i_now = 0
    while 1:
        if not old_str[i_old] == dont_want[i_dont]:
            return old_str[i_res:]
        i_now += 1
        # 1234
        # 12
        if i_now - i_res == dont_want_len:
            i_res += dont_want_len
        if i_dont == min_len - 1 or i_old == min_len - 1:
            return old_str[i_res:]

        i_old += 1
        i_dont += 1


# https://zhuanlan.zhihu.com/p/93671522


def camel(s):
    s = re.sub(r"(_|-)+", " ", s).title().replace(" ", "")
    return s[0].lower() + s[1:]


# 批量转化


def batch_camel(slist):
    return [camel(s) for s in slist]


def sentence_to_classname_or_methodname(sentence, which):
    out_str = ""
    len_sentence = len(sentence)

    upper = True if which == "class" else False
    for i in range(len_sentence):
        if sentence[i] == " ":
            upper = True
            continue
        else:
            if upper:
                out_str += sentence[i].upper()
                upper = False
            else:
                out_str += sentence[i]

    return out_str


def sentence_to_classname(sentence):
    """
    把句子转化为类名，就是弄个大写
    :param sentence:
    :return:
    """

    return sentence_to_classname_or_methodname(sentence, "class")


def test_sentence_to_classname():
    print(sentence_to_classname("a good boy"))


# 进一步扩展到全角数字
# https://www.runoob.com/python3/python3-check-is-number.html
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    import unicodedata
    try:
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
        
    if len(s) < 2:
        return False

    try:
        d = 0
        if s.startswith('－'):
            s = s[1:]
        for c in s:
            if c == '－': # 全角减号
                return False
                
            if c == '．': # 全角点号
                if d > 0:
                    return False
                else:
                    d = 1
                    continue
            unicodedata.numeric(c)
        return True
    except (TypeError, ValueError):
        pass

    return False


# https://www.runoob.com/python3/python3-upper-lower.html
def toCamel(string):
    out_str = ""
    title = 0
    str_len = len(string)
    for i in range(str_len):
        if string[i] == "_":
            title = 1
            continue
        if title == 1:
            title = 0
            out_str += string[i].upper()
        else:
            out_str += string[i]

    return out_str.replace("\n", ";\n")


def sentence_to_methodname(sentence):
    return sentence_to_classname_or_methodname(sentence, "method")


def dot_to_get_set(dot_string: str, type="set"):
    # p[0].name = "zhangsan";
    instanceNameAndOther = dot_string.split(".")
    instanceName = instanceNameAndOther[0]
    propertyAndVal = instanceNameAndOther[1].split("=")
    property = propertyAndVal[0].strip()
    val = propertyAndVal[1].strip().strip(";")
    return instanceName + "." + type + str.title(property) + f"({val});"


def dot_to_get_set_batch(dot_strings: list, type="set"):
    out_list = []
    for dot_string in dot_strings:
        out_list.append(dot_to_get_set(dot_string, type))

    return out_list


def modify_dot_str(dot_strings: str, type="set"):
    list_to_modify = dot_strings.split("\n")
    list_to_modify.remove("")
    for string in list_to_modify:
        if string.isspace():
            list_to_modify.remove(string)
    list_modified = dot_to_get_set_batch(list_to_modify, type)
    for string in list_modified:
        print(string)


def replace_all(old_str, be_replaced_dic):
    for key in be_replaced_dic:
        old_str = old_str.replace(key, be_replaced_dic[key])
    return old_str


def split_ques(string):
    len_str = len(string)
    for i in range(len_str):
        pass
        # todo
        # no do

def to_file_path_name(filename:str):
    filename=filename.strip()
    filename = filename.replace(" ", "_")
    # https://www.cnblogs.com/jjliu/p/11514226.html
    filename = filename.replace(":", "")
    return filename

def make_score_file_beautiful():
    file = open("replaceStr.txt", "r", encoding="utf-8")
    data = file.read()
    file.close()

    print(data.replace(r"\n", "\n\n"))


def print_funcs(string: str):
    starts = ["void", "int", "bool", "vector"]
    lines = string.split("\n")
    for line in lines:
        for start in starts:
            if line.startswith(start) and line.endswith("{"):
                print(line)


def two_sides_add(add_str_left, middle_str, add_str_right, ):
    return add_str_left + middle_str + add_str_right


def print_without_preffix(string, preffix):
    print(string.replace(preffix, ""))
    # printf(string.replace(preffix, ""))


def put_chinese_after_english():
    chinese_str = """
F） 有竞争力
G） 承认
H） 意识
一） 欲望
J） 排除
K） 特色
五十） 孤独
M） 分开
N） 壮观的
O） 搜查令


    """
    english_str = """
F) competitive
G) conceded
H) consciousness
I) desires
J) excluded
K) feature
L) lonely
M) separate
N) spectacularly
O) warrant

    """

    chinese_list = chinese_str.split("\n")
    chinese_list.remove("")
    english_list = english_str.split("\n")
    english_list.remove("")
    cnt = 0
    for chinese_one_str in chinese_list:
        print(english_list[cnt], chinese_one_str)
        cnt += 1


def split_nums(nums_str="1, 2, 2, 3, 4, 4, 5, 5, 7, 9"):
    for num in nums_str.split(","):
        print(num.strip())


from listUtil import str_rets_kind_to_list

# https://blog.csdn.net/caroline_wendy/article/details/23438739
def string_reverse(string):
    return string[::-1]



# python  str reverse
def back_char_cnt(string,what):
    rev_string=string_reverse(string)
    cnt=0
    for ch in rev_string:
        if ch==what:
            cnt+=1
        else:
            break
    return cnt


from itertools import takewhile


def get_front_num(string):
    # https://blog.csdn.net/weixin_35949386/article/details/114913828
    res = ''.join(takewhile(str.isdigit, string))
    return res


def create_tbl_sql_to_brackets(sql_str):
    # python re 找到 `` 包起来的
#     `logid` int(11) NOT NULL AUTO_INCREMENT,
#   `userid` int(11) DEFAULT NULL,
#   `username` varchar(255) DEFAULT NULL,
#   `faceid` int(11) DEFAULT NULL,
#   `facecontent` varchar(255) DEFAULT NULL,
#   `emotionid` int(11) DEFAULT NULL,
#   `emotioncontent` varchar(255) DEFAULT NULL,
#   `logtime` timestamp NULL DEFAULT NULL,
#   `logfaceresult` varchar(255) DEFAULT NULL,
#   `logemotionresult` varchar(255) DEFAULT NULL,
#   `logpicture` longblob,
#   `logresult` varchar(255) DEFAULT NULL,
    match_lst = re.findall('`.*`',sql_str)
    # print(m.group(0))
    # for match in m:
    #     print(match)
    # print(match_lst)
    # res="( "
    split=","
    res=split.join(match_lst)

    # res=match_lst.join(",")
    res="( "+res+")"
    print(res)
    return res
    # https://www.runoob.com/python3/python3-string-join.html
    # first=True
    # for match in match_lst:
    #     if first:
    #         res+=match.replace("`","")
    #         first=False
    #     else:
    #         res+=", "+match.replace("`","")

    # print(m.group(1))

def lst_put_together_end_not(lst,split):
    first=True
    res=""
    for val in lst:
        if first:
            res+=val
            first=False
        else:
            res+=split+val

    return res



def zhihu_name_put_follow(name_urls_str="""
https://www.zhihu.com/people/qing-gun-88-4
https://www.zhihu.com/people/na-sea
https://www.zhihu.com/people/miao-qi-pa
https://www.zhihu.com/people/xiayixuan""", follow_str="/following/topics"):
    lines = str_rets_kind_to_list(name_urls_str)
    for line in lines:
        print(line + follow_str)


def zhihu_name_put_follow_read_txt(txt_path, follow_str="/following/topics"):
    with open(txt_path, "r", encoding="utf-8") as f:
        name_urls_str = f.read()

    lines = str_rets_kind_to_list(name_urls_str)
    out_data = ""
    for line in lines:
        out_data += line + follow_str + "\n"

    out_txt_path = "topics_urls.txt"
    with open(out_txt_path, "w", encoding="utf-8") as f:
        f.write(out_data)
    print("那些人的关注话题网址，写在这个文件了", out_txt_path)


def lanqiao_have_put_in_pta():
    need_list = str_rets_kind_to_list("""小计算器
合根植物
分考场
小数第n位
对局匹配
发现环
区间移位
填字母游戏
图形排版
青蛙跳杯子
九宫幻方
Excel地址
k倍区间
日期问题
兰顿蚂蚁
分糖果
地宫取宝
蚂蚁感冒
城市建设
邮局
数字游戏
国王的烦恼
回文数字
公式求值
九宫重排
车轮轴迹
约数倍数选卡片
高僧斗法
网络寻路
危险系数
""")

def print_values(words):
    first=True
    print("values (",end='')
    for word in words:
        
        if first:
            first=False
        else:
            print(', ',end='')
        print("'",end='')
        print(word,end="'")
    # print()
    print(")",end='')

def list_add_dou_hao(string="""
D	2001	便携式电脑
D	2002	便携式电脑
E	2004	便携式电脑
D	3001	打印机
B	3002	打印机
A	1001	个人电脑
B	1004	个人电脑
D	1008	个人电脑

"""):
    lines=string.split("\n")
    for line in lines:
        if line=="":
            continue
        print("INSERT INTO product ",end=' ')
        words=line.split("\t")
        # print(words)
        first=True
        print_values(words)
        # for word in words:
           
        #     if first:
        #         first=False
        #     else:
        #         print(', ',end='')
        #     print(word,end='')
        print()
                

def css_replace(string):
    string=string.replace('//mc.stu.126.net/pub/s/pt_learn_learn_cc4c15bc2a2b6747962307bf201cc776.css',
    'https://mc.stu.126.net/pub/s/pt_learn_learn_cc4c15bc2a2b6747962307bf201cc776.css')
    return string
    
def mthml_replace(filename):
    with open(filename) as f:
        data=f.read()
    data=data.replace('<span class="u-icon-correct"></span>'
    ,'<span class="u-icon-correct">对</span>')
    # <span class="u-icon-wrong"></span>
    data=data.replace('<span class="u-icon-wrong"></span>'
    ,'<span class="u-icon-wrong">错</span>')
    filename_no_sufix=r_del_str(filename,".mhtml")
    
    out_filename=filename_no_sufix+"_replaced.mhtml"
    with open(out_filename,"w") as f:
        f.write(data)
    print("write at",out_filename)

if __name__ == "__main__":
    # put_chinese_after_english()
    # for i in range(1, 30 + 1):
    #     print(str(i) + ")")
    #     string = """
    # A) altemate B) crown C) determine D) generated E) locating F) merged G) miniatures H) opting I) particles J) peak K) prematurely L) simply M) swiching N) synonymous O) trend
    #     """

    # result = re.match( "itcast" , " itcast.cn " ) # match 第一个参数是需要匹配的字符串，第二个是源字符串
    # print("result:",result)
    # print(result.group())
    # print(ord("z"))
    # print(ord("Z"))
    # print(chr(137))
    # print(int("0xfffffffc",16))
    # print("0x7b integer")
    # print(int("0x7b",16))
    # print(int("0x1c8",16))
    # print(int("0xf",16))
    # https://www.runoob.com/python3/python3-ascii-character.html

    # finds=re.match("A",string).group()
    # # finds=re.match("[A-Z](.*)",string).group()
    # # re.match(pattern, string).group()
    # print(finds)
    # print(finds[1])
    # print(int('0.0'))
    # print(int(float('0.0')))
    # print(remove("我是大帅比", "帅"))
    # print(remove("我是大帅比  1", " "))
    # get_nums()
    # print("haha".encode("utf-8"))
    # print ('\u%04x' % ord("ch"))
    # print("\u%x"%ord("h"))
    # print("\u{}".format(ord("h")))
    # print(remove("55521 3    45  5553","5"))

    # str = 'åºéå¦!'
    # print(str_to_unicode(str))
    # print(front_del_str("1233", "12"))
    # print(front_del_str("1233", "1"))
    # print(front_del_str("1233", "1233"))
    # print(front_del_str("1233", "a1233"))
    # print(sentence_to_classname("a good boy"))
    # print(sentence_to_methodname("area of a pentagon"))
    # dot_string="p[0].age = 18;"
    # dot_strings = """
    #  p[1].name = "lisi";
    #     p[1].age = 20;
    #     p[2].name = "wangwu";
    #     p[2].age = 22;
    # """
    # print(dot_to_get_set(dot_string, type="get"))
    # modify_dot_str(dot_strings,"set")
    # print(str_to_unicode(" "))
    # print(str_to_unicode("26-35: IOJBC KHDAF"))

    # print(str.replace("`",""))
    # batch_sql_insert_str()
    # print(one_slash_to_two(r"D:\file\mingw-w64\mingw64\bin"))
    # print('C:\mingw64\lib\gcc\x86_64-w64-mingw32\8.1.0\include'.replace("\\","/"))
    # remove_dont_want_sql_elm(" m1.*,m2.`id` as id2,m2.`enabled` as enabled2,m2.`iconCls` as iconCls2")
    # test_re()
    # test_unicode()
    # string = """
    #     Mark Bezos is a volunteer firefighter in his town. At his first fire he was the second volunteer to arrive, It was raining in the middle of the night，but the homeowner was standing in the rain，with no shoes。
    #      The captain asked the other volunteer to rescue a dog from inside the house 。Mark Bezos felt jealous that the other volunteer could tell people he saved a living animal。While the captain asked Mark Bezos to go into the house and bring back some shoes。So ， he carried the shoes back downstairs and gave them to the homeowner。 A few weeks later， the homeowner sent a letter thanking the fire department，in particular for saving her shoes。
    #      Mark Bezos has learned that all the acts of kindness and generosity matter ，whether they are big or small。And he has sent the message to the audience；“don‘t wait util you make your first million to make a difference in somebody’s life。If you have something to give，give it now。“

    #     In my opinion， it was not a normal story，because being a firefighter is a valiant action，bringing back shoes for a person that with no shoes in the raining night is a valuable performance。And we know that a thank can cheer others up，so we should remember to say thank you when we need。
    # """
    # replace_dic = {
    #     "，": ",",
    #     "。": ".",
    #     "“": "\"",
    #     "”": "\"",
    #     "‘": "'",
    #     "’": "'"
    # }
    # print(replace_all(string, replace_dic))
    # row1 = ["facebok", 0.0, "usd", 31231, 3.5]
    # row2 = ["insta", 0.0, "usd", 13341241, 4.5]
    # print(str(row1[-4]+row2[-4])+'$')

    # for start in starts:
    #     funcs=sub_strs_start_end_all(string,start,"{")
    #     for func in funcs:
    #         print(r_del_str(func,"{"))

    # print(toCamel(string))
    strs = """共同特征
脊索
位于消化道和神经管之间的一条棒状结构，具有支持功能，所有脊索动物的胚胎期具有脊索，但在以后的生活中或终生保留（尾索动物亚门、头索动物亚门），或退化并被脊柱（vertebral column）代替。
脊索来源于胚胎期的原肠背壁，即脊索中胚层。经加厚、分化、外突，最后脱离原肠而成脊索。脊索由富含液泡的脊索细胞组成，外面围有脊索细胞所分泌而形成的结缔组织性质的脊索鞘（notochordal sheath）。脊索鞘常包括内外两层，分别为纤维组织鞘（fibrous sheath）和弹性组织鞘（elastic sheeth）。充满液泡的脊索细胞由于产生膨压，使整条脊索既具弹性，又有硬度， 从而起到骨骼的基本作用。
低等脊索动物中，脊索终生存在或仅见于幼体时期。高等脊索动物只在胚胎期间出现脊索，发育完全时即被分节的骨质脊柱（vertebral column）所取代。组成脊索或脊柱等内骨骼（endoskeleton）的细胞，都能随同动物体发育而不断生长。而无脊椎动物则缺乏脊索或脊柱等内骨骼，通常仅身体表面被有几丁质等外骨骼（exoskeleton）。脊索的出现在动物演化史上具有重要意义。表现在：
①脊索（以及脊柱）构成支撑躯体的主梁，是体重的受力者，也是内脏器官得到有力的支持和保护。
②运动肌肉获得坚强的支点，在运动时不致由于肌肉的收缩而使躯体缩短或变形，因而向“大型化”发展。同时，脊索的中轴支撑作用也能使动物体更有效地完成定向运动，对于主动捕食及逃避敌害都更为准确、迅速。
③脊椎动物头骨的形成、颌的出现以及椎管对中枢神经的保护，都是在此基础上进一步完善化的发展。
脊髓（dorsal tubular nerve cord）
位于脊索背面中空管状的中枢神经系统。脊椎动物神经管前端膨大成脑，脑后部分形成脊髓。
由胚体背中部的外胚层内陷形成。背神经管在高等种类中前、后分化为脑和脊髓。神经管腔（neurocoele）在脑内形成脑室（cerebral ventricle），在脊髓中成为中央管（centralcanal）。无脊椎动物神经系统的中枢部分为一条实性的腹神经索（ventral nerve cord），位于消化道的腹面。 [1]
    """
    # for s in strs.split("\n"):
    #     print(two_sides_add('<p>',s,"</p>"))
    # print(0xe)
    # print("%c"%0x78)
    # for i in range(3):
    #     print("%x"%(0x8+i*4))

    # print(14 >> 0x1f)
    # print(0x1f)
    # print(14>>1)
    print(0x40 - 0x24)
