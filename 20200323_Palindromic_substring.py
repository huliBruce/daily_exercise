#input "babad"
#ouput "bab"


#input "cbbd"
#output "bb"

# hard code

# startIndex
# endIndex
# maxLen = 1


# i=0  i
# i=1  i+n 不同了  比较 i+n + x   + i-x  直到不同 或者没有

#brute-force

startIndex = 0
endIndex = 0

def  helpFun(s):
	stringLen = len(s)
	maxLen = 1
	i =0 
	while i < stringLen:
		n = 0
		while (i+n) < stringLen and s[i] == s[i+n]:
			n+=1
		n=n-1
		x = 0
		while (i+n+x) < stringLen and (i-x) >=0 and s[i+n+x] == s[i-x]:
			x+=1
		x=x-1
		lenGap = n+1+2*x

		if lenGap > maxLen:
			maxLen = lenGap
			startIndex = i-x
			endIndex = i +n +1 +x

		if n > 1:
			i = i+n
		else:
			i=i+1

		print(i)

	return maxLen,startIndex,endIndex


mystr = "dbabbbbc"
result = helpFun(mystr)

class Solution:
 def longestPalindrome(self, s: str) -> str:
        stringLen = len(str)
        maxLen = 1
        i=0 
        startIndex = 0
        endIndex = 0
        while i < stringLen:
			n = 0
			while (i+n) < stringLen and str[i] == str[i+n]:
				n+=1
			n=n-1
			x = 0
        	while (i+n+x) < stringLen and (i-x) >=0 and str[i+n+x] == str[i-x]:
            	x+=1
			x=x-1
			lenGap = n+1+2*x

			if lenGap > maxLen:
				maxLen = lenGap
				startIndex = i-x
				endIndex = i +n +1 +x

			if n > 1:
				i = i+n
			else:
				i=i+1
        
		return str




print(longestPalindrome(mystr))