class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        cnt = 0
        back = {0: -1}
        for i, num in enumerate(nums):
            cnt += 1 if num == 1 else -1
            if cnt in back:
                res = max(res, i - back[cnt])
            else:
                back[cnt] = i

        return res
