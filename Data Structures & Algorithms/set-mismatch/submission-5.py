class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        p = set()
        expected= set(range(1, len(nums) + 1))
        s, q = 0, 0 

        for i in range(len(nums)):
            if nums[i] in p:
                s = nums[i]
            
            else:
                p.add(nums[i])
        q = list(expected.difference(p))[0]
            

        return [s, q]
        