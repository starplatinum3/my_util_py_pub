seats = list(map(int, input().strip().split()))
n = len(seats)
# 先找到左边第一个1出现的索引
edge = seats.index(1)
l_bound = edge
r_bound = n - 1
# 再找右边第一个1出现的索引，两者选大的作为边缘最大的距离
for i in range(n - 1, -1, -1):
    if seats[i] == 1:
        # 左边和右边大的一个
        edge = max(edge, n - 1 - i)
        right = i
        break
# 对于从left~right的子数组，寻找其中两个相邻1最大的距离即可
distance = 0
ones_idx = [l_bound]
for i in range(l_bound + 1, r_bound + 1):
    if seats[i] == 1:
        distance = max(distance, i - ones_idx[-1])
        ones_idx.append(i)
print(max(edge, distance // 2))