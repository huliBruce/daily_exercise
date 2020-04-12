# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6]        n = 3
# Output: [1,2,2,3,5,6]

# nums1 = [3,7,9,0,0,9], m = 3
# nums2 = [2,5,6]        n = 3

# nums1 = [2,7,9,0,0,0],   m = 3
# nums2 = [3,5,6]        n = 3


# end  = m+n -1
# pointerA = m-1
# pointerB = n-1



# int temp

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    	pointerA = m -1
    	pointerB = n -1
    	pointerTarget = m + n -1

    	while pointerA >= 0 and pointerB >= 0:
    		if nums1[pointerA] > nums2[pointerB]:
    			nums1[pointerTarget] = nums1[pointerA]
    			pointerTarget -=1
    			pointerA -= 1
    		else:
    			nums1[pointerTarget] = nums2[pointerB]
    			pointerTarget -=1
    			pointerB -= 1
    	while pointerB >= 0:
    		nums1[pointerTarget] = nums2[pointerB]
    		pointerTarget -=1
    		pointerB -=1

    	print(nums1)
   

s = Solution()
nums1 = [5,6,7,0,0,0]
nums2 = [2,5,6]
s.merge(nums1,3,nums2,3)



