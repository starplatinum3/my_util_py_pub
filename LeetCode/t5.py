
# LeetCodeUtil.
# from LeetCode.LeetCodeUtil import printLstMarked

from LeetCodeUtil import printLstMarked

class Solution:
    def longestPalindrome(self, s: str) -> str:
        le=len(s)
        if le==1:
            return s
        if le==2:
            if s[0]==s[1]:
                return s
            else:
                return s[0]
        dp=[]
        for i in range(le):
            dp.append([])
            for j in range(le):
                dp[i].append(0)
        dp[0][0]=1
        if s[0]==s[1]:
            dp[0][1]=2
        else:
            dp[0][1]=1
        dp[1][1]=1
        maxi=0
        maxj=0
        max_num=0
        for i in range(le):
           for j in range(i,le):
                if i-1<0 or j+1>=le:
                    continue
                if s[i-1]==s[j+1]:
                    # print("i",i)
                    # print("j",j)
                    printLstMarked(s,[i,j])
                    dp[i][j]+=2
                    dpp=dp[i][j]
                    print("dpp")
                    print(dpp)
                    val=dp[i][j]
                    if dp[i][j]>max_num:
                        max_num=val
                        maxi=i-1
                        maxj=j+1
                        print("maxi")
                        print(maxi)
                        print("maxj")
                        print(maxj)
        # for i in range(le):
        #    for j in range(i,le):

        print("maxi",maxi)
        print("maxj",maxj)
        return s[maxi:maxj+1]


Solution=Solution()
# val=Solution.longestPalindrome("babad")
val=Solution.longestPalindrome("cbbd")

print("val")
print(val)