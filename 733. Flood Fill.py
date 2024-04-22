class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m,n = len(image),len(image[0])
        queue = [(sr,sc)]
        match = image[sr][sc]
        to_change = [(sr,sc)]
        while queue:
            r,c = queue.pop()
            for I,J in (r+1,c),(r-1,c),(r,c+1),(r,c-1):
                if 0<=I<m and 0<=J<n and image[I][J]==match:
                    to_change.append((I,J))
                    image[I][J] = -1
                    queue.append((I,J))
        for i,j in to_change:
            image[i][j]=color
        return image