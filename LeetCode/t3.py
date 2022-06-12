# from turtle import seth
from LeetCodeUtil import printLstMarked


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        setHave=set()
        max_len=0
        len_s=len(s)
        while j<len(s):
            # abca
            print("==========")
            printLstMarked(s,[i,j])
            ch=s[j]
            while i<len_s and s[i]==ch:
                i+=1
            # if s[j] in setHave:
                
            #     print("in set")
            #     printLstMarked(s,[j])
            #     # tmp_len=j-i-1
            #     # if tmp_len>max_len:
            #     #     max_len=tmp_len
            #     #     print("i",i)
            #     #     print("j",j)
            #     # max_len=max(max_len,j-i)
            #         # printLstMarked(s,[i,j])
            #     ch=s[j]
            #     setHave.remove(ch)
            #     print("rm")
            #     print("setHave")
            #     print(setHave)
            #     # rmVal=s[i]
            #     # setHave.remove(rmVal)
            #     while i<len_s and s[i]==ch:
            #         i+=1
            #         # j+=1
            #     # j+=1
            #     # i+=1
                
            if s[j] not in setHave:
                tmp_len=j-i
                if tmp_len>max_len:
                    max_len=tmp_len
                    print("lenger")
                    printLstMarked(s,[i,j])
                    print("i",i)
                    print("j",j)
                setHave.add(s[j])
                print("add")
                print("setHave")
                print(setHave)
                j+=1
                
                
        print(max_len)


Solution=Solution()
Solution.lengthOfLongestSubstring("abcabcbb")
# Solution.lengthOfLongestSubstring("bbbbb")
# Solution.lengthOfLongestSubstring("pwwkew")


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         l=-1
#         r=0
#         n=len(s)
#         occ=set()
#         max_len=0
#         while True:
#             # for i in range(l,r):
#             i=0
#             if s[i] in occ:
#                 occ.pop()
#             while r<n and s[r] not in occ:
#                 # 右边的放进去
#                 occ.add(s[r])
#                 r+=1
#                 max_len=max(max_len,len(occ))
#
