class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        end = len(nums)
        for ind, assume_first_val in enumerate(nums, start=0):
            assume_second_val = target - assume_first_val
            Sublist =nums[0:ind] + nums[ind+1:]
            if assume_second_val in Sublist:
                return [ind, nums.index(assume_second_val, ind+1, end)]