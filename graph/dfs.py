# 深度遍历，非递归实现
class Solution(object):
    def maxAreaOfIsland(self, grid):
        maxn = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    print('调用dfs：')
                    maxn = max(maxn,self.dfs(grid,i,j))
        return maxn

    def dfs(self,grid,i,j):
        s = [[i,j]] # 定义栈
        grid[i][j] = 0
        rn = 0
        rn += 1
        print(grid)
        while s:
            i,j = s[-1]
            print(i,j)
            print(grid)
            if i-1>=0 and grid[i-1][j] >0:
                s.append([i-1,j])
                rn += 1
                i = i - 1
                grid[i][j] = 0
                continue
            if j-1>=0 and grid[i][j-1]>0:
                s.append([i,j-1])
                rn += 1
                j = j - 1
                grid[i][j] = 0
                continue
            if i+1<len(grid) and grid[i+1][j] >0:
                s.append([i+1,j])
                rn += 1
                i = i + 1
                grid[i][j] = 0
                continue
            if j+1 < len(grid[0]) and grid[i][j+1]>0:
                s.append([i,j+1])
                rn += 1
                j = j + 1
                grid[i][j] = 0
                continue
            s.pop()
        return rn

grid = [[0,1],[1,1]]
s = Solution()
print('结果是:%d'%s.maxAreaOfIsland(grid))
