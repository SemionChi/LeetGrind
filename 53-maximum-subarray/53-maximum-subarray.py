class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_p=nums[0]
        curr_sum=0
        for i in nums:
            if curr_sum<0:
                curr_sum=0
            curr_sum+=i
            max_p=max(max_p,curr_sum)
        return max_p
            
            
                
                    