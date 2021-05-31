class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        
        if len(s) < k: return False
        
        char_map = {}
        
        for c in s:
            char_map[c] = char_map.get(c, 0) + 1
        
        num_odd = 0
        for v in char_map.values():
            if v % 2 != 0: num_odd += 1
        
        return num_odd <= k