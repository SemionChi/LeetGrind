class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res={}
        if len(nums)<=1:
            return False
        if len(nums)%2==0:
            
            
            l,r=0,len(nums)-1

            while l<=r:
                if nums[l] not in res:
                    res[nums[l]]=1
                else:
                    return True
                if nums[r] not in res:
                    res[nums[r]]=1
                else:
                    return True
                l+=1
                r-=1
                
        else:
            res[nums[0]]=1
            l,r=1,len(nums)-1
            while l<=r:
                if nums[l] not in res:
                    res[nums[l]]=1
                else:
                    return True
                if nums[r] not in res:
                    res[nums[r]]=1
                else:
                    return True
                l+=1
                r-=1
            
        return False
        
        