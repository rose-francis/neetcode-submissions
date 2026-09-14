class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q=collections.deque([[sr,sc]])
        c=image[sr][sc]
        if c==color:
            return image
        m=len(image)
        n=len(image[0])
        while q:
            i,j=q.popleft()
            if image[i][j]==c:
                image[i][j]=color
                if i-1>=0:
                    q.append([i-1,j])
                if i+1<m:
                    q.append([i+1,j])
                if j-1>=0:
                    q.append([i,j-1])
                if j+1<n:
                    q.append([i,j+1])

        return image
