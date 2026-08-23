class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        wordmap1 = dict()
        wordmap2 = dict() 
        
        if (len(s) != len(t)):
            return False 

        for i in s:
            if i in wordmap1:
                wordmap1[i] = wordmap1[i] + 1
            else:
                wordmap1[i] = 1 
        
        for j in t:
            if j not in wordmap1:
                return False
            if j in wordmap2:
                wordmap2[j] = wordmap2[j] + 1
            else:
                wordmap2[j] = 1
        
        for key, value in wordmap2.items():
            if wordmap2[key] != wordmap1[key]:
                return False

        return True 