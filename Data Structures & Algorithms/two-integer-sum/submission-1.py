class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        search = dict()

        for i in range(len(nums)):
            search[nums[i]] = i
        
        for i in range(len(nums)):
            difference = target - nums[i]
            if (difference in search) and (search[difference] != i):
                return [i, search[difference]]

        # for i in range(len(nums)):
        #     difference = target - nums[i]
        #     if (difference in nums) and 
        # for key, value in search.items():
        #     difference = target - value
        #     if difference in search.values():
        #         for key1, value1 in search.items():
        #             if (value1 == difference) and (key1 != key):
        #                 output.append(key)
        #                 output.append(key1)
        #                 return(output)


        # for i in range(len(nums)):
        #     difference = target - nums[i]
        #     for j in range(1, len(nums)):
        #         if (difference == nums[j]) and (i != j):
        #             output.append(i)
        #             output.append(j)
        #             return(output)
        

        