class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = dict()
        for i in nums:
            if i in vals:
                vals[i] += 1
            else:
                vals[i] = 1
            
        elems = sorted(vals.values(), reverse=True)[:k]
        sol = list()
        for key, value in vals.items():
            if value in elems:
                sol.append(key)
        return sol


            
