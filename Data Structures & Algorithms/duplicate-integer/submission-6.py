class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        con_dup = {}
        for i in nums:
            if i in con_dup.keys():
                print(i)
                return True
            con_dup[i] = 1
            
        return False
            # if i in con_dup:
            #     return True