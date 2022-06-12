from functools import reduce
from operator import or_
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr, cnt = 0, 0
        for i in range(1, 1 << len(nums)):
            # val=(i >> j) & 1
            print("nums")
            print(nums)
            for j, num in enumerate(nums):
                val=(i >> j) & 1
                if (i >> j) & 1:
                    print("val")
                    print(val)
            # j 代表了 娶了或者不取得
            # 11101001 比如 i 是这个 ，j 是某个 往右移动，那么
            # 1110(1)001 比如这一个就会被往右移动
            # 1110(1) &1 就代表这一位他是有1 的，也就是这几位有数字
            orVal = reduce(or_, (num for j, num in enumerate(nums) if (i >> j) & 1), 0)
            if orVal > maxOr:
                maxOr, cnt = orVal, 1
            elif orVal == maxOr:
                cnt += 1
        return cnt

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/count-number-of-maximum-bitwise-or-subsets/solution/tong-ji-an-wei-huo-neng-de-dao-zui-da-zh-r6zd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

Solution=Solution()
Solution.countMaxOrSubsets([3,1])