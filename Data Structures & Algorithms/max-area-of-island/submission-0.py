class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        visit = set()

        def bfs(i,j, area):
            queue = collections.deque()
            queue.append((i,j))
            visit.add((i,j))
            while queue:
                r,c = queue.popleft()
                dir =[[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in dir:
                    row = r + dr
                    col = c + dc
                    if row in range(rows) and col in range(cols) and \
                         grid[row][col] == 1 and (row,col) not in visit:
                         queue.append((row, col))
                         visit.add((row, col))
                         area += 1
            return area


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visit:
                    area = bfs(i,j,1)
                    max_area = max(max_area, area)
        return max_area
        