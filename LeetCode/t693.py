
# num=7
# num=5
# last=0
# fir=True
# while num>0:
#     # print(num)
#     mod=num%2
#     if fir:
#         last=mod
#         fir=False
#     else:
#         if last==mod:
#             return False
#     print(num%2)
#     num//=2
    # num%
    
# from cmath import log


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # num=5
        num=n
        last=0
        fir=True
        while num>0:
            # print(num)
            mod=num%2
            if fir:
                last=mod
                fir=False
            else:
                if last==mod:
                    return False
                last=mod
            # print(num%2)
            num//=2
            # num%
        return True


Solution=Solution()
# n=11
n=5
res=Solution.hasAlternatingBits(n)
print("res")
print(res)