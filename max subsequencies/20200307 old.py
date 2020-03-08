import time


def  LCS(s1,s2):
	return helper(s1,s2,0,0)

def  helper(s1,s2,i1,i2):
	if i1 == len(s1) or i2 == len(s2):
		return ''

	if s1[i1] == s2[i2]:
		return s1[i1] + helper(s1,s2,i1+1,i2+1)

	resultA = helper(s1,s2,i1+1,i2)
	resultB = helper(s1,s2,i1,i2+1)

	if len(resultA) > len(resultB):
		return resultA
	else:
		return resultB


textA = 'ABCDEDDDF'
textB = 'ACDEGSDFSDFS'

start_time = time.time()
result = LCS(textA,textB)
end_time = time.time()

print(end_time - start_time)
print(result)