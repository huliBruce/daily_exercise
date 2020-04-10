import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
    	val = math.sqrt(c)
    	x, y = 0, int(val)
    	while x != y:
    		result = x*x + y*y
    		if result == c:
    			return True
    		elif result < c:
    			x+=1
    		else:
    			y-=1
    	return False



# a*a + b*b = c 
# c1 

c = Solution()
b = c.judgeSquareSum(3)
print(b)
