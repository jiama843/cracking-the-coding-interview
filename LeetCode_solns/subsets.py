def combine(sub1, sub2):
    all_subs = sub1 + sub2
    for s1 in sub1:
        for s2 in sub2:
            all_subs.append(s1 + s2)

    return all_subs

def subsets_r_help(nums):
    if len(nums) == 0: return []
    if len(nums) == 1: return [nums]
    
    mid = len(nums)/2
    l_sub = subsets_r_help(nums[0: mid])
    r_sub = subsets_r_help(nums[mid: len(nums)])
    
    return combine(l_sub, r_sub)
    

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        return [[]] + subsets_r_help(nums)