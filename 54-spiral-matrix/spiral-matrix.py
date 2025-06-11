class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        l,t = 0,0
        b = m-1
        r = n-1
        direction = 0
        ans = []
        while l<=r and t<=b:
            #top row
            if direction==0:
                for i in range(l,r+1):
                    ans.append(matrix[t][i])
                t += 1
            #right column
            elif direction==1:
                for i in range(t,b+1):
                    ans.append(matrix[i][r])
                r -= 1
            #bottom row
            elif direction==2:
                for i in range(r,l-1,-1):
                    ans.append(matrix[b][i])
                b -= 1
            #left column
            else:
                for i in range(b,t-1,-1):
                    ans.append(matrix[i][l])
                l += 1

            direction = (direction+1)%4        
        
        return ans