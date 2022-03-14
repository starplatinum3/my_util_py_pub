class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)
        while l<=r:
            mid=(l+r)/2
            
