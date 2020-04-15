from collections import deque

class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        s = deque([x for x in s])
        for each in shift:
            if each[0] == 0:
                s.rotate(-1 * each[1])
            else:
                s.rotate(each[1])
        return "".join(s)
