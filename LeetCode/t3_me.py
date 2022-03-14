class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        setHave=set()
        max_len=0
        while j<len(s):
            # abca 
            if s[j] in setHave:
                max_len=max(max_len,j-i)
                j+=1
                i+=1
            else:
                
                setHave.add(s[j])
                j+=1
        print(max_len)

        # l=-1
        # r=0
        # n=len(s)
        # occ=set()
        # max_len=0
        # while True:
        #     # for i in range(l,r):
        #     i=0
        #     if s[i] in occ:
        #         occ.pop()
        #     while r<n and s[r] not in occ:
        #         # 右边的放进去
        #         occ.add(s[r])
        #         r+=1
        #         max_len=max(max_len,len(occ))


Solution=Solution()
# Solution.lengthOfLongestSubstring("abcabcbb")
# Solution.lengthOfLongestSubstring("bbbbb")
Solution.lengthOfLongestSubstring("pwwkew")
        

