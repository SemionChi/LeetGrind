class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        res=max(nums)
        while l<=r:
           
            if nums[r]>nums[l]:
                res=min(res,nums[l])
                break
            m= (l+r)//2
            res = min(res,nums[m])
            if nums[m]>=nums[l]:
                l=m+1
            else:
                r=m-1
        return res