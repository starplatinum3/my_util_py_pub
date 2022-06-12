# from operator import le
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return list({'()'})
        res = set()
        for lowRes in self.generateParenthesis(n - 1):
            # 用更少的去找到他们的组合
            print("=========")
            print("lowRes")
            print(lowRes)
            # 加上了旁边的括号吗
            len_all=len(lowRes) + 2
            print("len_all",len_all)
            for j in range(len(lowRes) + 2):
                # 在中间插入
                res.add(lowRes[0:j] + '()' + lowRes[j:])
        return list(res)

        # https://leetcode-cn.com/problems/generate-parentheses/solution/gua-hao-sheng-cheng-by-leetcode-solution/


Solution=Solution()
Solution.generateParenthesis(4)