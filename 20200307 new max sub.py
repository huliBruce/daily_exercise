import time

def  LCS(s1,s2):
	h1 = len(s1)
	h2 = len(s2)
	print((h1,h2))
	memo = [[0 for i in range(h2)] for j in range(h1)]
	return helper(s1,s2,0,0,memo)

def  helper(s1,s2,i1,i2,memo):
	if i1 == len(s1) or i2 == len(s2):
		return ''

	if memo[i1][i2] != 0:
		return memo[i1][i2]

	if s1[i1] == s2[i2]:
		memo[i1][i2] = s1[i1] + helper(s1,s2,i1+1,i2+1,memo)
		return memo[i1][i2]

	resultA = helper(s1,s2,i1+1,i2,memo)
	resultB = helper(s1,s2,i1,i2+1,memo)

	result = ''
	if len(resultA) > len(resultB):
		result = resultA
	else:
		result = resultB

	memo[i1][i2] = result
	return memo[i1][i2]


textA = 'ABCDEDDDF'
textB = 'ACDEGSDFSDFS'


start_time = time.time()
result = LCS(textA,textB)
end_time = time.time()

print(end_time - start_time)
print(result)