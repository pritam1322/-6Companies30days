class Solution:
    def Anagrams(self, words, n):
    
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        res = []
        d = dict()
        for w in words:
            s = "".join(sorted(w))
            if s in d.keys():
                d[s] += ' '+w
            else:
                d[s] = w 
                
        for k,v in d.items():
            res.append(v.split(" "))
        
        return res
                
                
        
        
        

