def significant_number(arr):
	d=1
	sum=0
	for ele in arr[::-1]:
		sum=sum+ele*d
		d=d*10
	return sum+1


arr=[1,2,3]
result=significant_number(arr)
print(result)

