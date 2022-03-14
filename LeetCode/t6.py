# from tkinter.messagebox import NO


# from curses.ascii import SO

# from os import access


# ac

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        i=0
        j=0
        mat=[]
        col_cnt=len(s)/4*2+10
        col_cnt=int(col_cnt)
        for ii in range(numRows):
            mat.append([])
            for jj in range(col_cnt):
                mat[ii].append(None)
        print(mat)
        s_idx=0
        xie=False
        while True:
            if s_idx>=len(s):
                break
            ch=s[s_idx]
            print("ch",ch)
            # print()
            print("i",i)
            print("j",j)
            mat[i][j]=s[s_idx]
            s_idx+=1
            # if(i==numRows-1):
            #     # i-=1
            #     # j+=1
            #     xie=True
            # elif i==0:
            #     # i+=1
            #     xie=False
            if i==0:
                xie=False
            elif(i==numRows-1):
                xie=True
            # i+=1
            if xie:
                i-=1
                j+=1
            else:
                i+=1
            # if(i==numRows-1):
            #     # i-=1
            #     # j+=1
            #     xie=True
            # elif i==0:
            #     # i+=1
            #     xie=False
        res=""
        # for ii in range(col_cnt):
        #     for jj in range(numRows):
        #         cell= mat[jj][ii]
        #         if mat[jj][ii]==None:
        #             continue
        #         # res+=mat[ii][jj]
        #         res+=cell

        for ii in range(numRows):
            for jj in range(col_cnt):
                # cell= mat[jj][ii]
                cell= mat[ii][jj]
                if cell==None:
                    continue
                # res+=mat[ii][jj]
                res+=cell
        print(res)
        return res




Solution=Solution()
# Solution.convert("AB",1)
# Solution.convert("PAYPALISHIRING",3)

Solution.convert("ABC",1)

