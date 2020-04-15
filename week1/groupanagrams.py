from itertools import groupby
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        return [list(group) for key,group in groupby(sorted(strs,key=sorted),sorted)]
