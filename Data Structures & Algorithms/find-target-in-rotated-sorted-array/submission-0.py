class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            # Found the target
            if nums[m] == target:
                return m
            
            # Check if left half is sorted
            if nums[l] <= nums[m]:
                # Target is in the sorted left half
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:  # Right half is sorted
                # Target is in the sorted right half
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1  # Target not found