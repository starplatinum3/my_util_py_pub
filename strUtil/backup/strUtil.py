# from appdirs import unicode
# from numpy import unicode
import re


def make_str_some_what(str: str, wholeLen: int, what: str):
    lenStr = len(str)
    toAdd = wholeLen - lenStr
    prefix = ""
    for i in range(toAdd):
        prefix += what

    return prefix + str


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
    return instanceName+"."+type+str.title(property)+f"({val});"


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


def make_score_file_beautiful():
    file = open("replaceStr.txt", "r", encoding="utf-8")
    data = file.read()
    file.close()

    print(data.replace(r"\n", "\n\n"))



if __name__ == "__main__":
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
    dot_strings = """
     p[1].name = "lisi";
        p[1].age = 20;
        p[2].name = "wangwu";
        p[2].age = 22;
    """
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
    string="""
    //
// Created by Lenovo on 2020/10/29.
//


#include <stdio.h>


const int maxn = 1000010;
const int MAX_STU_NUM = 30000;
int maxPersonCnt = 0;
int f[maxn];
int howManyPersons[maxn + 1];
int vis[maxn];

void init() {
    int i;
    for (i = 0; i <= maxn; i++) {
        f[i] = i;
    }
}


void initWithPersonCnt(int howMany[]) {
    int i;
    for (i = 0; i <= maxn; i++) {
        f[i] = i;
        howMany[i] = 1;
    }
}

void initWithPersonCnt() {
    int i;
    for (i = 0; i <= maxn; i++) {
        f[i] = i;
        howManyPersons[i] = 1;
    }
}

int find(int x, int fatherSet[]) {
    if (x != fatherSet[x])
        return fatherSet[x] = find(fatherSet[x], fatherSet);
    else
        return x;
}


int find(int x) {
    return find(x, f);
}


void uni(int x, int y) {
    int fx = find(x);
    int fy = find(y);
    if (fx != fy)f[fx] = fy;
}

void uniteWithPersonCnt(int x, int y, int howMany[]) {
    int fx = find(x);
    int fy = find(y);
    if (fx != fy) {
        howMany[fy] += howMany[fx];
        howMany[fx] = 0;
        if (howMany[fy] > maxPersonCnt)
            maxPersonCnt = howMany[fy];
//        howMany[fx]=0;
        f[fx] = fy;
    }
}

void uniteWithPersonCnt(int x, int y) {
    int fx = find(x);
    int fy = find(y);
    if (fx != fy) {
        howManyPersons[fy] += howManyPersons[fx];
        howManyPersons[fx] = 0;
        if (howManyPersons[fy] > maxPersonCnt)
            maxPersonCnt = howManyPersons[fy];
//        howMany[fx]=0;
        f[fx] = fy;
    }
}

#include <stdlib.h>
#include <cstring>
#include <vector>

void uniteVector(std::vector<int> v) {
    int mainNum = v[0];
    for (int i = 1; i < v.size(); i++) {
        uni(mainNum, v[i]);
    }
}

int max(int arr[], int len) {
    int maxCount = arr[0];
    for (int i = 1; i < len; i++) {
        if (maxCount < arr[i])maxCount = arr[i];
    }
    return maxCount;
}

//获得最大集团里面有多少人的个数
/**
 * 获得最大集团里面有多少人的个数
 * @param fromIndex 从哪个人开始找，这个是他的编号
 * @param toIndex 找到哪个人为止，这个是他的编号
 * @param fatherSet 并查集的集合，如果提供一个null的话，用的是全局变量的f，不然就是传进来的这个
 * 主要是find(i, fatherSet) 函数的区别
 * @return 获得最大集团里面有多少人的个数
 */
int getCountOfBiggestSet(int fromIndex, int toIndex, int fatherSet[]) {
//        输出给出一个整数，表示在最大朋友圈中有多少人。
    int kingHaveHowManyServants[MAX_STU_NUM];
    memset(kingHaveHowManyServants, 0, sizeof(int) * MAX_STU_NUM);
    for (int i = fromIndex; i <= toIndex; i++) {
//        f[i] is  i's father ,不一定的，有些好像还没有设置为他的最大的老大哥, how many the father king of all them
        int fatherNum;
        if (fatherSet) {
            fatherNum = find(i, fatherSet);
        } else {
            fatherNum = find(i);
        }

        kingHaveHowManyServants[fatherNum]++;

    }
    int maxCount = kingHaveHowManyServants[0];
    for (int i = 1; i < MAX_STU_NUM; i++) {
        if (maxCount < kingHaveHowManyServants[i])maxCount = kingHaveHowManyServants[i];
    }
    return maxCount;
}

void testDisjointSet() {

    init();
    int n, m;
//      分别代表学校的学生总数和俱乐部的个数
    scanf("%d%d", &n, &m);
    for (int i = 0; i < m; i++) {
        int howMany;
        scanf("%d", &howMany);

        int headNum;
        for (int j = 0; j < howMany; j++) {
            int stuNum;
            scanf("%d", &stuNum);
            if (j == 0)headNum = stuNum;
            else {
                uni(headNum, stuNum);
            }
        }
    }


    int maxNum = getCountOfBiggestSet(1, n, nullptr);
    printf("%d\n", maxNum);
}

#include <algorithm>
#include <functional>

bool haveSameHobby(std::vector<int> person1, std::vector<int> person2) {
    for (int hobby:person1) {
        if (std::find(person2.begin(), person2.end(), hobby) != person2.end()) {
            return true;
        }
    }
    return false;
}

int getCountOfSets(int n) {
    int cnt = 0;
    for (int i = 1; i <= n; i++) {
//        找到它的大王就是他自己，那就是一个集合了
        if (find(i) == i) {
            cnt++;
        }
    }
    return cnt;
}

//7-1 社交集群 (30分)
void socialSet() {
    int n, m;
//      分别代表学校的学生总数和俱乐部的个数
    scanf("%d", &n);
//    int howManyPersons[n+7];
    initWithPersonCnt();
//    ，n 为社交网络平台注册的所有用户的人数

    using namespace std;
    vector<vector<int>> persons(n + 1);
    for (int i = 1; i <= n; i++) {
        int howMany;
        scanf("%d:", &howMany);

//        int headNum;
        for (int j = 0; j < howMany; j++) {
            int hobby;
            scanf("%d", &hobby);
            persons[i].push_back(hobby);

        }
    }

    for (int i = 1; i <= n; i++) {
        for (int j = i + 1; j <= n; j++) {
            if (i != j && haveSameHobby(persons[i], persons[j]))
                uniteWithPersonCnt(i, j);
        }
//        if (haveSameHobby(persons[i], persons[1])) {
//            uniteWithPersonCnt(1, i);
//        }
    }
//    首先在一行中输出不同的社交集群的个数。随后第二行按非增序输出每个集群中的人数。数字间以一个空格分隔，行末不得有多余空格。

    int cnt = getCountOfSets(n);
//    int howManyInThisSet[n+7];
//    memset(howManyInThisSet,0, sizeof(int)*(n+7));
//    for (int i = 1; i <= n; i++) {
//        int fi = find(i);
////       howManyInThisSet[fi]++;
//        howManyPersons[fi]++;
//    }
    vector<int> setCounts;
    printf("%d\n", cnt);
    for (int i = 1; i <= n; i++) {
//        if(howManyInThisSet[i]>0){
//            printf("%d ",howManyInThisSet[i]);
//        }

        if (howManyPersons[i] > 0) {
            setCounts.emplace_back(howManyPersons[i]);
//            printf("%d ", howManyPersons[i]);
        }
    }
//    https://blog.csdn.net/lytwy123/article/details/84503492
    sort(setCounts.begin(), setCounts.end(), std::greater<int>());
    int first=1;
    for (int setCount:setCounts) {
        if(first){
            printf("%d", setCount);
            first=0;
        }else{
            printf(" %d", setCount);
        }


    }
//    int maxNum = getCountOfBiggestSet(1, n, nullptr);
//    printf("%d\n", maxNum);
}

//int main(){
//     socialSet() ;
//}

    """
    starts=["void","int","bool","vector"]
    lines=string.split("\n")
    for line in lines:
        for start in starts:
            if line.startswith(start) and line.endswith("{"):
                print(line)
    # for start in starts:
    #     funcs=sub_strs_start_end_all(string,start,"{")
    #     for func in funcs:
    #         print(r_del_str(func,"{"))

    # print(toCamel(string))
