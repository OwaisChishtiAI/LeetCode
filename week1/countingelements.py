class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        for each in arr:
            if each + 1 in arr:
                count += 1
        return count
