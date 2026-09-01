class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_group = dict()
        for i in strs:
            reorg = ''.join(sorted(i))
            if reorg in sorted_group:
                sorted_group[reorg].append(i)
            else:
                sorted_group[reorg] = [i]
            
        return list(sorted_group.values())