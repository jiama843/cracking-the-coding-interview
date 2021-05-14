class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        
        dup_map = {}
        lst_tuples = []
        
        for i in range(0, len(values)):
            lst_tuples.append((values[i], labels[i]))

        lst_tuples = sorted(lst_tuples, reverse=True)
        
        ret_sum = 0
        sub_size = 0
        for l in lst_tuples:
            if sub_size >= num_wanted: break
            
            dup_map[l[1]] = dup_map.get(l[1], 0) + 1

            if dup_map[l[1]] > use_limit: continue
            
            ret_sum += l[0]
            sub_size += 1

        return ret_sum