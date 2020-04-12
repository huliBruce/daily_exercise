#
#   fib(n) = fib(n-1) + fib (n-2)
#   if n ==1 or n== 2 return 1
#  1 1 2 3 5 8 13 
#  memoized solution
# O(2^n) -> O(n)

def fib(n):
	mem = [None] * (n+1)
	return helper(n,mem)

def helper(n,mem):
	if n == 1 or n ==2:
		mem[n] = 1
		return mem[n]
	if mem[n] is not None:
		return mem[n]
	mem[n] = helper(n-1,mem) + helper(n-2,mem)
	return mem[n]

#we don't need to worry about recursive calls
def fib_bottom_up(n):  
	if n ==1 or n==2:
		return 1
	bottom_up = [None]*(n+1)
	bottom_up[1] = 1
	bottom_up[2] = 1
	for i in range(3,n+1):
		bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
	return bottom_up[n]

#result = fib(1000)
result2 = fib_bottom_up(10000)
#print(result)
print(result2)
