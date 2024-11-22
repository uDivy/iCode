class Solution:
    def pivotInteger(self, n: int) -> int:
        left_sum = 0
        total_sum = n * (n + 1) // 2
        
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            left_sum = (mid * (mid - 1)) // 2
            right_sum = total_sum - left_sum - mid
            
            if left_sum < right_sum:
                low = mid + 1
            elif left_sum > right_sum:
                high = mid - 1
            else:
                return mid
        
        return -1
        