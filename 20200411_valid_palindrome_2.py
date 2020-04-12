#input "abca"
#output True

# abac 

# aacca
# 前后两个是否相同 往中间走 hasChance
# 去掉前面 是否相同 往中间走 noChance
# 去掉后面 是否相同 往中间走 noChance





#class Solution:
#	def helper(self, temp:list) -> bool:
#		start,end = 0,len(temp) -1;
#		while start < end:
#			if temp[start] == temp[end]:
#				start +=1
#				end -=1
#			else:
#				return False
#		return True#

#	def validPalindrome(self, s: str) -> bool:
#		temp = list(s)
#		if self.helper(temp) == True:
#			return True#

#		for i in range(0,len(s)):
#			temp = list(s)
#			temp.pop(i)
#			if self.helper(temp) == True:
#				return True
#		return False


#第一种方法超时

#尝试第二种方法
#要么删除左边的，要么删除右边的，要么不删除 就三种可能
#这个题遇到了坑 脑子不好用 aabc
 
class Solution:
	def helper(self,s: str,start:int,end:int) -> bool:
		print([start,end])
		while start < end:
			if s[start] == s[end]:
				start +=1
				end -=1
			else:
				return False
		return True
		
	def validPalindrome(self, s: str) -> bool:
		start, end = 0, len(s) -1
		while start < end:
			if s[start] == s[end]:
				start +=1
				end -=1
			else:
				return self.helper(s,start+1,end) or self.helper(s,start,end-1)
		return True


s = Solution()
val = s.validPalindrome("abc")
print(val)

