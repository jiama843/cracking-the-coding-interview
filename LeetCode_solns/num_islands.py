class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def connected(grid, r, c):
            if r < 0 or r > len(grid) - 1: return False
            if c < 0 or c > len(grid[-1]) - 1: return False
            if grid[r][c] == "0": return False
            
            return True

        def bfs(adj_lst, s):
            queue = []
            visited = set()
            
            queue.append(s)
            visited.add(s)
            
            while len(queue) > 0:
                v = queue.pop(0)
                
                for neighbour in adj_lst[v]:
                    if neighbour not in visited:
                        queue.append(neighbour)
                        visited.add(neighbour)

            return visited
        
        adj_lst = {}
        
        for r in range(0, len(grid)):
            for c in range(0, len(grid[-1])):
                if grid[r][c] == "0": continue
                
                dirs = []
                
                # left
                if connected(grid, r, c-1): dirs.append((r, c-1))
                    
                # right
                if connected(grid, r, c+1): dirs.append((r, c+1))
                    
                # up
                if connected(grid, r-1, c): dirs.append((r-1, c))
                    
                # down
                if connected(grid, r+1, c): dirs.append((r+1, c))
                
                adj_lst[(r, c)] = adj_lst.get((r, c), [])
                adj_lst[(r, c)] += dirs
        
        num_islands = 0
        while len(adj_lst) > 0:
            s = adj_lst.keys()[-1]
            
            island_nodes = bfs(adj_lst, s)
            
            for node in list(island_nodes): adj_lst.pop(node, None)
            
            num_islands += 1
        
        return num_islands