#coding=utf-8

# print(1)

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         print(1)

from __future__ import print_function
# from lib2to3.pgen2.pgen import DFAState


from operator import le

# ac  python2 import 不要

class Solution:
    # vis
    def dfs(self,x,y):
        pass
        self.vis[x][y]=True
        if x==3 and y==3:
            # print("3 is dfs ed")
            pass
        for dir in self.dirs:
            # dir[0]
            nx=dir[0]+x
            ny=dir[1]+y
            if nx==3 and ny==3:
                print("how ",x,y)
                # 这里会跨过 0
            if nx>=self.m or nx<0 or ny>=self.n or ny<0:
                continue
            if self.vis[nx][ny]==True:
                continue
            if self.grid[nx][ny]=="0":
                continue
            # 访问的全部访问 就是一个岛屿
            # self.vis[nx]
            self.dfs(nx,ny)



    def numIslands(self, grid):
        #  def numIslands(self, grid) -> int:
    # def numIslands(self, grid:List[List[str]]) -> int:
        self.dirs=[[-1,0],[1,0],[0,-1],[0,1]]
        self.vis=[]
        self.m=len(grid)
        self.n=len(grid[0])
        self.grid=grid
        cnt=0
        for i in range(self.m):
            self.vis.append([])
            # self.vis[i]=[]
            for j in range(self.n):
                self.vis[i].append(False)
                # self.vis[i]=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==3 and j==3:
                    print("i,j,3")
                # print(i,j)
                    print("vis")
                    print(self.vis[i][j])
                if grid[i][j]=="1" and self.vis[i][j] ==False:
                    # print("i,j")
                    # print(i,j)
                    cnt+=1

                    self.dfs(i,j)
                    pass
        print("cnt",cnt)
        return cnt

def make_matrix(m,n):
    grid=[]
    for i in range(m):
        grid.append([])
        # self.vis[i]=[]
        for j in range(n):
            grid[i].append(None)
    return grid

def print_matrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j],end=" ")
            # print mat[i][j] 
            # python 2 print end
        print()
# grid=[]
grid=[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
# m=3
# n=3
print_matrix(grid)

# for i in range(m):
#     grid.append([])
#     # self.vis[i]=[]
#     for j in range(n):
#         grid[i].append("1")
print("grid")
print(grid)
Solution=Solution()
Solution.numIslands(grid)