/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map1 = new Map();
    for (var i=0;i<nums.length;i++) {
        var diff=target-nums[i];
        if (map1[diff]!==undefined){
            return [map1[diff],i];
        }else{
            map1[nums[i]]=i;
        }
        
    }
    
    
};