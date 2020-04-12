from typing import List

class Solution:
	"""docstring for Solution"""
	def twoSum(self, numbers:List[int],target:int)->List[int]:
		x = 0
		y = len(numbers) - 1
		result = []
		while x != y :
			temp = numbers[x] + numbers[y]
			if temp == target:
				result.append(x)
				result.append(y)
				return result
			elif temp > target:
				y = y -1
			else :
				x = x +1

	def twoSum2(self, numbers:List[int],target:int)->List[int]:
		low, high = 0, len(numbers)-1
		print(low,high)
		while low != high:
			sum2 = numbers[low] + numbers[high]
			if sum2 == target:
				return low+1,high +1 
			elif sum2 < target:
				low += 1
			else:
				high -=1


	def twoSum3(self, numbers:List[int],target:int)->List[int]:
		dic = {}
		for i,num in enumerate(numbers):
			if target - num in dic:
				return dic[target-num] + 1,i+1
			dic[num] = i


#由低到高排序 
# x= 0  y = len     a[x] + a[y] =  target return x y    
# < x ++
# > y ++

s = Solution()
a = [1,2,3,9]
b = s.twoSum3(a,10)
print(b)


		