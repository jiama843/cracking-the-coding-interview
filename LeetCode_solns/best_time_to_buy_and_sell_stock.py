class Solution(object):

    # IV
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        def max_pst_table(prices):
            P = [0] * len(prices)

            smallest_so_far = prices[0]
            for i in range(1, len(prices)):
                P[i] = max(prices[i] - smallest_so_far, P[i-1])

                smallest_so_far = min(smallest_so_far, prices[i])

            return P
        
        def max_pst_table_rev(prices):
            P = [0] * len(prices)

            max_so_far = prices[len(prices) - 1]
            for i in range(len(prices) - 2, -1, -1):
                P[i] = max(max_so_far - prices[i], P[i+1])

                max_so_far = max(max_so_far, prices[i])

            return P
        
        t1 = max_pst_table(prices)
        t2 = max_pst_table_rev(prices)
        
        max_so_far = 0
        for i in range(0, len(t1)):
            max_so_far = max(max_so_far, t1[i] + t2[i])
        
        return max_so_far
        