#https://www.youtube.com/watch?v=GBuHSRDGZBY
#https://www.csdojo.io/problem
#不需要获取坐标，只需要把两个数字找出来
#起名字的时候尽量取的易懂一些
#尽量定义函数
#如何保留多个坐标？

#    x x x x V
#    x x x x x
#    x x x x x
#    x x x x x


def cloest_sum_pair(a1,a2,target):
	a1_sorted = sorted(a1)
	a2_sorted = sorted(a2)
	keyY = 0
	keyX = len(a2) - 1
	smallest_diff = abs(a1_sorted[0] + a2_sorted[0] - target)
	cloest_pair = (a1_sorted[0],a2_sorted[0])

	while keyY < len(a1) and keyX >=0 :
		v1 = a1_sorted[keyX]
		v2 = a2_sorted[keyY]
		current_diff = v1 + v2 - target
		if abs(current_diff) < smallest_diff:
			smallest_diff = abs(current_diff)
			cloest_pair = (v1,v2)

		if current_diff == 0:
			return cloest_pair

		if current_diff > 0:
			keyX -= 1
		else:
			keyY += 1
	return cloest_pair


b1 = [7, 4, 1, 10]
b2 = [4, 5, 8, 7]
b_target = 13

reuslt = cloest_sum_pair(b1,b2,b_target)

print(reuslt)

	
