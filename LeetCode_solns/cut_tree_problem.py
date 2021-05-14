# 675. Cut Off Trees for Golf Event
# Last testcase is incorrect

def bfs(start, end, adj):
    if start == end: return 0
    
    dist = 0
    
    queue = []
    visited = set()
    
    queue.append((start, 0))
    visited.add(start)
    
    while len(queue) > 0:
        v, dist = queue.pop(0)

        for neighbour in adj[v]:
            if neighbour not in visited:
                queue.append((neighbour, dist + 1))
                visited.add(neighbour)
                if neighbour == end: return dist + 1

    return -1


def blocked(dir_, forest):
    r, c = dir_

    return forest[r][c] == 0


def in_bounds(dir_, num_row, num_col):
    r, c = dir_
    if r < 0 or r >= num_row:
        return False

    if c < 0 or c >= num_col:
        return False

    return True

class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        
        adj_lst = {}
        pq_tree_order = []
        
        for r, row in enumerate(forest):
            for c, col in enumerate(row):

                curr = (r, c)
                
                if forest[r][c] > 1: pq_tree_order.append((forest[r][c], curr))
                
                left = (r, c - 1)
                right = (r, c + 1)
                up = (r - 1, c)
                down = (r + 1, c)
                
                if in_bounds(left, len(forest), len(row)) and not blocked(left, forest):
                    adj_lst[curr] = adj_lst.get(curr, [])
                    adj_lst[curr].append(left)
                
                if in_bounds(right, len(forest), len(row)) and not blocked(right, forest):
                    adj_lst[curr] = adj_lst.get(curr, [])
                    adj_lst[curr].append(right)
                
                if in_bounds(up, len(forest), len(row)) and not blocked(up, forest):
                    adj_lst[curr] = adj_lst.get(curr, [])
                    adj_lst[curr].append(up)
                
                if in_bounds(down, len(forest), len(row)) and not blocked(down, forest):
                    adj_lst[curr] = adj_lst.get(curr, [])
                    adj_lst[curr].append(down)
        
        # print(adj_lst)
        
        heapq.heapify(pq_tree_order)

        total_dist = 0
        start_point = (0, 0)
        while len(pq_tree_order) > 0:
            if start_point not in adj_lst: return -1
            
            next_point = heapq.heappop(pq_tree_order)[-1]
            #print(next_point)
            
            curr_dist = bfs(start_point, next_point, adj_lst)
            #print(curr_dist)

            if curr_dist < 0: return -1

            total_dist += curr_dist
            start_point = next_point

        return total_dist
