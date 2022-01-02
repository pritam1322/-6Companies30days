class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2 :
            return  str1
        elif str1+str2 != str2+str1 :
            return ""
        
        else:
            len_by_gcd = math.gcd(len(str1), len(str2))
            return self.gcdOfStrings(str1[:len_by_gcd],str2[:len_by_gcd]) 
        
        
        
        
        
        

