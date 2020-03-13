#https://www.youtube.com/watch?v=GBuHSRDGZBY
#https://www.csdojo.io/problem
#如何将最后获取的坐标和sort前的坐标对应起来
#如何保留多个坐标
#    x x x x V
#    x x x x x
#    x x x x x
#    x x x x x

arrayA = [1,2,5]
arrayB = [-2,0,1]

keyNumber = 4

arrayA.sort()
arrayB.sort()

print(len(arrayA))


lenArray = len(arrayA) 
keyA = lenArray -1
keyB = 0

position = [-1,-1]
minNumber = keyNumber


for keyB in range(0,lenArray):
	totalNumber = arrayA[keyA] + arrayB[keyB] 

	if totalNumber == keyNumber:
		position[0] = keyA
		position[1] = keyB
		break

	if abs(totalNumber - keyNumber) <  minNumber:
		position[0] = keyA
		position[1] = keyB

	if totalNumber > keyNumber:
		if(keyA > 0):
			keyA -= 1
		else:
			break

print(position)
