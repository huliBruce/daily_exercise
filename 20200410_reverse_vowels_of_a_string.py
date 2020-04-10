# a e i o u 

# abcie

class Solution:
    def reverseVowels(self, s: str) -> str:
    	start, end = 0, len(s) -1
    	sTemp = list(s)
    	vowel = ['a','e','i','o','u','A','E','I','O','U']
    	while start < end:
    		if sTemp[start] in vowel and sTemp[end] in vowel:
    			temp = sTemp[end]
    			sTemp[end] = sTemp[start]
    			sTemp[start] = temp
    			start += 1
    			end -=1 
    		elif sTemp[start] in vowel:
    			end -=1
    		elif sTemp[end] in vowel:
    			start +=1
    		else:
    			start += 1
    			end -=1 
    	return ''.join(sTemp)
   
    


s = Solution()
print(s.reverseVowels("leetcode"))
