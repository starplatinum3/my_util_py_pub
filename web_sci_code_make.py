cols="""
Publication_Year_col=Col2Int('AU')-1
Article_Title_col=Col2Int('I')-1
Start_Page_col=Col2Int('BB')-1
End_Page_col=Col2Int('BC')-1"""

lines=cols.split("\n")

print(lines)

for line in lines:
    if line =="":
        continue
    sps=line.split("_col")
    name=sps[0]
    # print(name)
    print(f"{name} = sh.cell_value(val_row,{name}_col)")