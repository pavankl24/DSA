class Solution(object):
    def runningSum(self,nums):
        for num in range(1,len(nums)):
            nums[num]+=nums[num-1]
        return nums
    
sum=Solution()
num_list=[1,2,3,4]
result=sum.runningSum(num_list)
print(result)