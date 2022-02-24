class Solution(object):
    def move(self,row_num):
        for row in self.grid:
            # col=row[]
            col=0
            # 这一列的方向 和
            if col<0 or col>=len(row) or row[col]!=col:

        # for row in self.grid[row_num]:
            # 这一行在往右走吗
            
        # self.grid=row
        
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        # grid 的所有行数
        n=len(grid)
        col_num=len(grid[0])
        self.grid=grid
        for col in range(col_num):
            self.move(col)
        # for i in n:
        #     move(i)
