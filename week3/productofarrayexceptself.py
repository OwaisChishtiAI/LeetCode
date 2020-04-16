class Solution:
    def productExceptSelf(self, nums):
        if not nums:
            return []

        out = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            out[i] = out[i - 1] * nums[i - 1]

        prod = 1
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i + 1]
            out[i] = out[i] * prod

        return out
