import re

from AsmKind import AsmKind
from Operand import Operand

def sizeof(type):
    if type=="short":return 2
def cal_arr_addr(addr,index,type):
    """
    打印某个地址开头数组的下标为index的地址是什么
    :param addr:
    :param index:
    :param type:
    :return:
    """
    # print("arr from",addr,"index of",index,"is",hex(addr+index*sizeof(type)))
    print(f"arr{[0]}'s addr is",hex(addr))
    print("计算过程: addr+index*sizeof(type)")
    print(f"arr{[index]}'s addr is",hex(addr+index*sizeof(type)))
def memoryAsmExplain(memoryAsm: str, type):
    # 16(%ebp), %eax
    # scaleFactor
    # scaleFactorAndOther=memoryAsm.split("(")
    # scaleFactor=scaleFactorAndOther[0]
    # other=scaleFactorAndOther[1]
    # https://cloud.tencent.com/developer/ask/63918

    # re.search('^(\d+):([\d.]+) (\w+),(\w+)$',memoryAsm).groups()
    # searchObj = re.search('(\d*)\(%(.+),*%*(.*),(\d*)\)', memoryAsm)
    # searchObj = re.search('(\d*)', memoryAsm)
    # searchObj = re.search('(.*)\(%*(.*),*%*(.*),*(.*)\)', memoryAsm)

    memoryAsm = memoryAsm.strip()
    # print("memoryAsm:",memoryAsm)
    searchObj = re.search('(.*)\(%*(.*)\)', memoryAsm)
    # print("searchObj.group(0):",searchObj.group(0))
    addNum = searchObj.group(1)
    # baseReg=searchObj.group(2)
    threeThings = searchObj.group(2)
    threeThings = threeThings.split(",")
    # len_threeThings = len(threeThings)

    baseReg = threeThings[0]
    indexReg = None
    scaleFactor = None
    try:
        indexReg = threeThings[1]
    except IndexError:
        pass

    if indexReg:
        indexReg = indexReg.replace("%", "")
    try:
        scaleFactor = threeThings[2]
    except IndexError:
        pass

    # indexReg=searchObj.group(3)
    # scaleFactor=searchObj.group(4)
    #     int addNum;
    # char baseReg[3];
    # char indexReg[3];
    # //    char scaleFactor[3];
    # int scaleFactor;
    # print("1: ", searchObj.group(1))
    # print("2: ", searchObj.group(2))
    # print("3: ",searchObj.group(3))
    # print("4: ",searchObj.group(4))
    if type == AsmKind.LEA:
        explainStr = ""
    else:
        explainStr = "M["
    # print("explainStr:",explainStr)
    explainStr += "R[" + baseReg + "]"
    if indexReg:
        # return f"R[{baseReg}+{indexReg}*{scaleFactor}]"
        explainStr += " + R[" + indexReg + "]"

    if scaleFactor:
        explainStr += " * " + scaleFactor

    if addNum:
        explainStr += " + " + addNum
    if not type == AsmKind.LEA:
        explainStr += "]"
    return explainStr
    # return searchObj


def movExplain(asm):
    return movOrLeaExplain(asm, AsmKind.MOV)


def leaExplain(asm):
    return movOrLeaExplain(asm, AsmKind.LEA)


def removeSomePreffix(string, dontWantList, dontWantSuffixList):
    # dataTypeSuffixes = ["b", "w", "l", "q"]

    for dontWant in dontWantList:
        if dontWant in string:
            # string=string.replace(dontWant,"")
            for dontWantSuffix in dontWantSuffixList:
                string = string.replace(dontWant + dontWantSuffix, "")
    for dontWant in dontWantList:
        string = string.replace(dontWant, "")
    return string


def movOrLeaExplain(movOrLeaStr: str, type=None):
    # 16(%ebp), %eax
    movOrLeaStr = movOrLeaStr.strip()
    if type is None:
        if movOrLeaStr.startswith("lea"):
            type = AsmKind.LEA
        else:
            type = AsmKind.MOV

    # print("movOrLeaStr:",movOrLeaStr)
    dontWantList = ["lea", "mov"]
    dataTypeSuffixes = ["b", "w", "l", "q"]
    movOrLeaStr = removeSomePreffix(movOrLeaStr, dontWantList, dataTypeSuffixes)
    # parseBinaryOperation()
    # print("movOrLeaStr:",movOrLeaStr)
    srcAsmExplain, dstAsmExplain = parseBinaryOperation(movOrLeaStr)

    return dstAsmExplain + "  ←  " + srcAsmExplain


def regOrMemoToExplain(regOrMemo: str, type):
    if "(" in regOrMemo:
        # memoryAsmExplain
        # regOrMemoAsmExplain=
        # print("regOrMemo:",regOrMemo)
        return memoryAsmExplain(regOrMemo, type)
    return "R[" + regOrMemo.replace("%", "") + "]"


def asmExplain(asmStr: str):
    lines = asmStr.split("\n")
    lines.remove("")

    print("lines", lines)
    for line in lines:
        line = line.strip()
        # line=re.search("(.*)#*.*",line).group(1)
        pos = line.find("#")
        line = line[:pos]
        print("line:", line)
        if line.startswith("add"):
            print(addExplain(asmStr))
        elif line.startswith("sub"):
            print(subExplain(asmStr))
        elif line.startswith("lea"):
            print(leaExplain(asmStr))
        elif line.startswith("mov"):
            print(movExplain(asmStr))


def parseBinaryOperation(binaryOperation: str):
    src, dst = parseBinaryOperationToSrcAndDst(binaryOperation)
    # binaryOperation = binaryOperation.strip()
    # try:
    #     # splits = binaryOperation.split(")")
    #     splits = binaryOperation.split(",")
    #     # src = splits[0] + ")"
    #     src = splits[0]
    #     dst = splits[1].replace(",", "").strip()
    # except Exception:
    #
    #     splits = binaryOperation.split(",")
    #     src = splits[0]
    #     dst = splits[1].replace(",", "").strip()

    # print("dst:",dst)
    # print("src:",src)
    srcAsmExplain = regOrMemoToExplain(src, type)
    dstAsmExplain = regOrMemoToExplain(dst, type)
    return srcAsmExplain, dstAsmExplain


# operand 操作数
def parseBinaryOperationToSrcAndDst(binaryOperation: str):
    binaryOperation = binaryOperation.strip()
    try:
        # splits = binaryOperation.split(")")
        splits = binaryOperation.split(",")
        # src = splits[0] + ")"
        src = splits[0]
        dst = splits[1].replace(",", "").strip()
    except Exception:

        splits = binaryOperation.split(",")
        src = splits[0]
        dst = splits[1].replace(",", "").strip()

    src_obj = Operand(src)
    return src, dst


def addExplain(addStr: str):
    return addOrSubExplain(addStr, AsmKind.ADD)


def subExplain(subStr: str):
    return addOrSubExplain(subStr, AsmKind.SUB)


def addOrSubExplain(addOrSubStr: str, type=None):
    if type is None:
        if addOrSubStr.startswith("add"):
            type = AsmKind.ADD
        else:
            type = AsmKind.SUB

    dataTypeSuffixes = ["b", "w", "l", "q"]
    dontWantList = ["add", "sub"]
    addOrSubStr = removeSomePreffix(addOrSubStr, dontWantList, dataTypeSuffixes)
    # print("addOrSubStr:",addOrSubStr)
    srcAsmExplain, dstAsmExplain = parseBinaryOperation(addOrSubStr)
    return dstAsmExplain + "  ←  " + dstAsmExplain + (" + " if (type == AsmKind.ADD) else " - ") + srcAsmExplain


class Asm:
    INDEX_CODE_START = 32

    def __init__(self, address, code, src, dst):
        self.address = address
        self.code = code
        self.src = src
        self.dst = dst

    def asm_to_python_batch(self, asm_list):
        python_code = "#汇编 转化为python代码，版本v1\n"

        for asm in asm_list:
            code: str
            code = asm.code
            if code == "push   %ebp":
                python_code += "#保护上一个栈底\n"
            elif code == "mov    %esp,%ebp":
                python_code += "#栈底到的新的函数处\n"
            # if asm.code
            elif code.startswith("mov") or code.startswith("lea"):
                # todo
                pass

    def asm_to_python(self, asm_obj):
        code = asm_obj.code
        if code == "push   %ebp":
            return "#保护上一个栈底"
        elif code == "mov    %esp,%ebp":
            return "#栈底到的新的函数处"
        elif code.startswith("mov") or code.startswith("lea"):
            dontWantList = ["lea", "mov"]
            dataTypeSuffixes = ["b", "w", "l", "q"]
            movOrLeaStr = removeSomePreffix(code, dontWantList, dataTypeSuffixes)
            src, dst = parseBinaryOperationToSrcAndDst(movOrLeaStr)
            # todo
            return str(dst) + " = " + str(src)


# def esp_to_arr(esp_str):

# from ..strUtil.strUtil import front_del_str
# from strUtil.strUtil import front_del_str
from .strUtil import front_del_str


# ImportError: attempted relative import with no known parent package
#
# https://blog.csdn.net/qq_43355223/article/details/87340858
def str_to_asm_class(string):
    code = string[Asm.INDEX_CODE_START:]
    string = front_del_str(string, " ")
    address = string[0:string.find(":")]
    asm = Asm(hex(address), code)
    return asm


def para_num(esp_str: str):
    """
    esp+多少都是参数，我们要知道这个参数是第几个
    :param esp_str:
    :return:
    """
    if esp_str == "(%esp)":
        return 1
    num_and_esp = esp_str.split("(")
    # https://blog.csdn.net/ycf18331272870/article/details/88413838
    # print(int(num_and_esp[0],16))
    num = int(num_and_esp[0], 16) / 4 + 1
    return num


def print_para_num(esp_str: str):
    num = int(para_num(esp_str))
    print(esp_str, ":", "参数", num)


def print_para_num_batch(asm_str: str):
    """
    汇编的一些代码，esp+某个数字 的参数可以知道他是参数几
    :param asm_str:
    :return:
    """
    lines = asm_str.split("\n")
    failed = []
    for line in lines:
        if line == "": continue
        print(line)
        if line.endswith("(%esp)"):
            # format_str = "0x(.)(%esp)"
            # re.search("0x(.)(%esp)", line)
            searchObj = re.search('0x(.*)\(%esp\)', line)
            # print(line)
            # print("searchObj:",searchObj)
            if searchObj == None:

                if line[line.find("(%esp)") - 1] != "x":
                    print_para_num("(%esp)")
                else:
                    failed.append(line)
                continue
            num = searchObj.group(1)
            if "," in num:
                num = num.split(",")[1]
                esp_str = num + "(%esp)"
            else:
                esp_str = "0x" + num + "(%esp)"
            print_para_num(esp_str)

    print("failed:", failed)


if __name__ == "__main__":
    # print(memoryAsmExplain("0x16(%ebp,%eax,2)"))
    # print(memoryAsmExplain("0x16(%ebp,%eax)"))
    # print(memoryAsmExplain("16(%ebp)"))
    # print(movOrLeaExplain("16(%ebp), %eax", AsmKind.lea))
    # print(movOrLeaExplain("leal	(%eax,%eax,2), %eax "))
    # print(movOrLeaExplain("movl	12(%ebp), %edx "))
    # print(movOrLeaExplain("movl	%ebp, %edx "))
    # print(movOrLeaExplain("leal %ebp, %edx "))
    # print(addExplain("addl %ebp, %edx"))
    # print(addOrSubExplain("addl %ebp, %edx"))
    # print(addOrSubExplain("subl %ebp, %edx"))
    string = """
    movl	12(%ebp), %edx      #R[edx]  ←  M[ R[ebp] + 12]
	addl	8(%ebp), %edx           #
	andl	$65535, %edx           #
	"""
    asm_str = """
     8048f6b:	8b 45 08             	mov    0x8(%ebp),%eax
 8048f6e:	89 04 24             	mov    %eax,(%esp)
 8048f71:	e8 3a 00 00 00       	call   8048fb0 <strings_not_equal>
 8048f76:	85 c0                	test   %eax,%eax
 8048f78:	74 05                	je     8048f7f <phase_1+0x22>
 8048f7a:	e8 2e 02 00 00       	call   80491ad <explode_bomb>"""
    # print("asm_str:", asm_str)
    # asmExplain(string)  不行 效果不好
    # print(addExplain("andl	$65535, %edx "))
    # print(movOrLeaExplain("mov %eax,(%edx)"))
    # print(movExplain("mov %eax,(%edx)"))
    # print(movExplain("movl	12(%ebp), %eax "))
    # print(memoryAsmExplain("8(%ebp)",AsmKind.MOV))
    # print(subExplain("subl	16(%ebp), %eax "))
    # splits = "1".split(")")
    # print(AsmKind.mov)
    # print(movOrLeaExplain("mov %eax,(%edx)"))
    # print(movOrLeaExplain("movl %eax,(%edx)"))
    # print(addExplain("add %edx, %eax"))
    # print(" 8048ae0:	55                   	push   %ebp".find("push"))
    # print(para_num("0x10(%esp)"))
    print(parseBinaryOperation("%eax,(%esp)"))
