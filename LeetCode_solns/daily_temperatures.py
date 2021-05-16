class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        stack = []
        ret_temp_array = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            # print(stack)
            if len(stack) == 0:
                stack.append((i, t))
            elif stack[-1][1] < t:
                while len(stack) > 0 and stack[-1][1] < t:
                    elem = stack.pop()
                    ret_temp_array[elem[0]] = i - elem[0]
                stack.append((i, t))
            else:
                stack.append((i, t))
            
        return ret_temp_array