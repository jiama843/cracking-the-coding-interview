class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        v1_indexed = [int(i) for i in version1.split(".")]
        v2_indexed = [int(i) for i in version2.split(".")]
        
        comp_ver = v1_indexed if len(v1_indexed) < len(v2_indexed) else v2_indexed
        rem_ver = v1_indexed if len(v1_indexed) > len(v2_indexed) else v2_indexed
        
        for i in range(0, len(comp_ver)):
            if v1_indexed[i] > v2_indexed[i]:
                return 1
            elif v1_indexed[i] < v2_indexed[i]:
                return -1

        for i in range(len(comp_ver), len(rem_ver)):
            if rem_ver[i] > 0:
                return 1 if rem_ver == v1_indexed else -1
        
        return 0