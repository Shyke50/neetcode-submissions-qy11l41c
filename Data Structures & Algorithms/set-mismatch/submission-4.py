class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        p = set()
        
        s, q = 0, 0 

        for i in range(len(nums)):
            if nums[i] in p:
                s = nums[i]
            
            else:
                p.add(nums[i])
                for num in range(1, len(nums) + 1):
                    if num not in p:
                        q = num
                        break
            

        return [s, q]
        