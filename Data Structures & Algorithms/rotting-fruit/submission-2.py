class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        time = 0
        que = deque()
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    que.append([i, j])

        directions = [[0,1], [0, -1], [1,0], [-1,0]]

        while que and fresh > 0 : 
            for element in range(len(que)):
                r, c = que.popleft()
                for dr, dc in directions:
                    row = r+dr
                    col = c+dc
                    if (row < 0 or row == len(grid) or
                        col < 0 or col == len(grid[0]) or
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    que.append([row,col])
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
        
                         

