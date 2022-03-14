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


Solution=Solution()
# Solution.lengthOfLongestSubstring("abcabcbb")
# Solution.lengthOfLongestSubstring("bbbbb")
Solution.lengthOfLongestSubstring("pwwkew")