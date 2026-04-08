class Solution:
    def findMin(self, nums: List[int]) -> int:
       
        l, r = 0, len(nums) - 1
        minu = nums[0]
            
        while l <= r:
                # If current subarray is sorted
            if nums[l] < nums[r]:
                minu = min(minu, nums[l])  # Fixed: nums[l] not nums[1]
                break
                
            m = (l + r) // 2
            minu = min(minu, nums[m])  # Check middle element
                
            if nums[m] >= nums[l]:
                # Left portion is sorted, minimum is in right portion
                l = m + 1
            else:
                # Right portion is sorted, minimum is in left portion
                r = m - 1
            
        return minu