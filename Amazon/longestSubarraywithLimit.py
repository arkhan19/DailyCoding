class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        curr_min, curr_max = nums[0], nums[0]
        left = 0
        right = 1
        ans = 1

        while right < len(nums):
            # add nums[right] to lists
            curr_min = min(curr_min, nums[right])
            curr_max = max(curr_max, nums[right])
            while curr_max - curr_min > limit:
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                if curr_min == nums[left]:
                    curr_min = min(nums[left + 1:right + 1])
                if curr_max == nums[left]:
                    curr_max = max(nums[left + 1:right + 1])
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans