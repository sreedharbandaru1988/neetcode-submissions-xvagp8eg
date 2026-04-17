class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            queue = collections.deque()          
            visit.add((r,c))
            queue.append((r,c))

            while queue:
                row, col = queue.popleft()
                directions = [ [0,1], [0,-1],[1,0], [-1,0] ]
                for dr, dc in directions:
                    
                    if (row + dr in range(rows) and col + dc in range(cols) and \
                        grid[row+dr][col+dc] == "1" and (row+dr, col+dc) not in visit):
                        queue.append((row+dr, col+dc))
                        visit.add((row+dr, col+dc))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visit:
                    bfs(i, j)
                    islands += 1
        return islands

        