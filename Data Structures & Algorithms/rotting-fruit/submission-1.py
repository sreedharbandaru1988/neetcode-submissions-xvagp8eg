class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        rows, cols = len(grid), len(grid[0])      
        minutes = 0
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while queue and fresh > 0:
            for p in range(len(queue)):
                r, c = queue.popleft()
                directions = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh -= 1
                        queue.append((row,col))                              
            minutes += 1

        if fresh == 0:
            return minutes
        else:
            return -1