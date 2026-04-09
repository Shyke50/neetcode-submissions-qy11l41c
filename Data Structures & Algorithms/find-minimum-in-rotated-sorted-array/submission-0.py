class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        # Initialize minu with first element
        minu = nums[0]
        
        while l <= r:
            m = (l + r) // 2
            
            # Update minu with current mid value
            minu = min(minu, nums[m])
            
            # Check which side has the minimum
            if nums[m] > nums[r]:
                # Minimum is in right half
                l = m + 1
            else:
                # Minimum is in left half (including mid)
                r = m - 1
        
        return minu