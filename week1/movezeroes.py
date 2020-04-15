class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i] = nums[i]
            else:
                nums[i] = None
                count+=1
        for _ in range(count):
            nums.append(0)
        while(None in nums):
            nums.remove(None)
        return nums
