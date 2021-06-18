class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res_arr = [0] * (len(num1) + len(num2))
        
        for i, n1 in enumerate(num1):
            for j, n2 in enumerate(num2): 
                res_arr[i + j + 1] += int(n1) * int(n2)
        
        for i in range(len(res_arr) - 1, 0, -1):
            res_arr[i - 1] += res_arr[i]/10
            res_arr[i] %= 10
        
        while res_arr[0] == 0 and len(res_arr) > 1: res_arr.remove(0)
        
        return "".join([str(r) for r in res_arr])
