class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        n=0
        for i in nums:
            diff = target - i
            if diff in res:
                return [res[diff], n]
            res[i] = n
            nums[n]=None
            n+=1
        