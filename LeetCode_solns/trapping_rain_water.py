class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        arr_l = []
        arr_r = []
        
        max_height = 0
        
        for i in range(0, len(height)):
            max_height = max(height[i], max_height)
            arr_l.append(max_height)

        max_height = 0

        for i in range(len(height) - 1, -1, - 1):
            max_height = max(height[i], max_height)
            arr_r.append(max_height)
        
        arr_r.reverse()
            
        fin_cap = 0
        
        for i in range(0, len(height)):
            fin_height = min(arr_l[i], arr_r[i])
            fin_cap += fin_height - height[i]
        
        return fin_cap