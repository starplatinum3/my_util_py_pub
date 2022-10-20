import sys
# sys.path
print("sys.path")
print(sys.path)
import xlrd
#打开excel

def Col2Int(s:str)->int:
    # assert(isinstance(s, str))
    for i in s:
        if not 64<ord(i)<91:
            raise ValueError('Excel Column ValueError')
    return sum([(ord(n)-64)*26**i for i,n in enumerate(list(s)[::-1])])
 
# >>> Col2Int('A')
# 1
# >>> Col2Int('Z')
# 26
# >>> Col2Int('AA')
# 27
# >>> Col2Int('ZZ')
# 702
# >>> Col2Int('ZJX')
# 17860
# >>> Col2Int('ZZZ')
# 18278
# >>> 26*26**2+26*26+26
# 18278
# >>> Col2Int('ABCD')
# 19010
# >>> 1*26**3+2*26**2+3*26**1+4*26**0
# 19010
# >>> 
# conda activate py374
# D:\proj\python\my_util_py_pub>pip install xlrd
# ModuleNotFoundError: No module named 'xlrd'
# xlrd 读取 几行几列
# 获取sheet表单元格值
# cell_0_value = sheet_1.cell_value(0,0)
# print(cell_0_value)
file_name=r"D:\download\savedrecs.xls"
wb = xlrd.open_workbook(file_name)
# wb = xlrd.open_workbook('test_user_data.xlsx')
#按工作簿定位工作表
# sh = wb.sheet_by_name('TestUserLogin')
sh = wb.sheet_by_name('savedrecs')
print("sh.nrows")
print(sh.nrows)#有效数据行数
print("sh.ncols")
print(sh.ncols)#有效数据列数
print("sh.cell(0,0).value 输出第一行第一列的值")
print(sh.cell(0,0).value)#输出第一行第一列的值
print("输出第一行的所有值")
print(sh.row_values(0))#输出第一行的所有值
#将数据和标题组合成字典
print("将数据和标题组合成字典")
print(dict(zip(sh.row_values(0),sh.row_values(1))))
#遍历excel，打印所有数据
print("遍历excel，打印所有数据")
for i in range(sh.nrows):
    print(sh.row_values(i))


val_row=1
Authors_col=1
Publication_Year_col=Col2Int('AU')-1
Article_Title_col=Col2Int('I')-1
Start_Page_col=Col2Int('BB')-1
End_Page_col=Col2Int('BC')-1

print("Publication_Year_col",Publication_Year_col)
# Article Title
# Publication_Year_col 46
# val_row=2
# val_row=1
j_int=Col2Int('J')
# Source_Title_col_int=Col2Int('J')
print("j_int",j_int)
# Source_Title_col_int=10
# 要 -1 
Source_Title_col_int=9
# cell_0_value = sh.cell_value(0,0)
# print(cell_0_value)
Source_Title_val = sh.cell_value(val_row,Source_Title_col_int)
Authors = sh.cell_value(val_row,Authors_col)
Publication_Year = sh.cell_value(val_row,Publication_Year_col)
Publication_Year=int(Publication_Year)
Article_Title = sh.cell_value(val_row,Article_Title_col)

# Publication_Year = sh.cell_value(val_row,Publication_Year_col)
# Article_Title = sh.cell_value(val_row,Article_Title_col)
Start_Page = sh.cell_value(val_row,Start_Page_col)
Start_Page=int(Start_Page)
End_Page = sh.cell_value(val_row,End_Page_col)
End_Page=int(End_Page)
# Publication_Year = sh.cell_value(val_row,Publication_Year_col)
# Publication_Year = sh.cell_value(val_row,Publication_Year_col)
# Publication_Year_col=Col2Int('AU')-1
# Article_Title_col=Col2Int('I')-1
# Start_Page_col=Col2Int('BB')-1
# End_Page_col=Col2Int('BC')-1
print("Source_Title_val")
print(Source_Title_val)
# j_int 10
# Publication Type
cite_str=f"{Authors}. {Article_Title}.{Source_Title_val}.{Publication_Year}:{Start_Page}-{End_Page}"

# cite_str=f"{Authors}. {Article_Title_col}.{Source_Title_val}.{Publication_Year_col}:{Start_Page_col}-{End_Page_col}"
print(cite_str)
# D:\proj\python\my_util_py_pub>python --version
# Python 3.7.4

# 查看python路径 