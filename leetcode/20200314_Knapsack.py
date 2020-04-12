# weight 1	2	4	2	5
#  value 5	3	5	3	2
# total weigths = 10

#recursive solution
#1  helper(i+1,total_weight)
#2  helper(i+1,total_weigth - wight[i])

weight = [1,2,4,2,5]
value = [5,3,5,3,2]

max_weight  = 10
weight_len = len(weight)

arr = [[None for i in range(max_weight + 1)] for j in range(weight_len + 1)]

#像这种函数，最多只有n*total_weight个解
def helper(i,total_weight):
	if i == len(weight) - 1 or total_weight <= 0:
		return 0

	if arr[i][total_weight] is not None:
		return arr[i][total_weight]


	value1 = value[i] + helper(i+1,total_weight - weight[i])
	value2 = helper(i+1,total_weight)

	max_value = max(value1,value2)
	arr[i][total_weight] = max_value

	return max_value

result = helper(0,10)
print(result)



	





		
	

