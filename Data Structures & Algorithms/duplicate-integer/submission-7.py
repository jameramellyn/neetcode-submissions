class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        con_dup = dict()
        for i in nums:
            if i in con_dup:
                return True
            else:
                con_dup[i] = 1
        return False
        