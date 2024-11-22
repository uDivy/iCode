class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Initialize slow and fast pointers
        slow = nums[0]
        fast = nums[0]
        
        # Move slow by one step and fast by two steps
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Find the entry point of the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow  # The duplicate number
        