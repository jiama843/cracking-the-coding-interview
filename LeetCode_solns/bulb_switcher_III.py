class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        
        count = 0
        lbits = 0
        
        sig_lbit = 0
        
        for l in light:
            lbits += (1 << (l-1))
            sig_lbit = max(sig_lbit, (1 << l) - 1)
            
            if sig_lbit == lbits: count += 1
        
        return count